## Install required libs
import os
from functions import segmentation_models_pytorch as smp
import albumentations as albu

import torch
import numpy as np
from torch.utils.data import DataLoader
from  torch.utils.data import Dataset as BaseDataset
from scipy.ndimage import gaussian_filter
import scipy.ndimage as ndimage
import matplotlib

import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
import json
import math

from functions.utils import *


#######################################################################
############################## LOAD DATA ##############################
#######################################################################

output_path = './results/segment/'
create_subfolders_output(output_path, ['models', 'logs', 'images'])

from parameters import *

##########TO CHANGE ##############

# RE
root = root_directory_re
classes_dataset = classes_re
classes_names = classes_names_re
colors_list = colors_list_re

# KI67 
# root = root_directory_ki67#_v2
# classes_dataset = classes_ki67
# classes_names = classes_names_ki67
# colors_list = colors_list_ki67

len_classes = len(classes_dataset)

ori_path = root + 'Images/'
gt_path = root + 'Cells/'
sufix = '.GT_cells'

# split randomly (80-20)
x_train, y_train, x_valid, y_valid = split_dataset(ori_path, gt_path, sufix)
print(len(x_train))
print(len(x_valid))

# split per patients (option: removing 2 images with only stroma)
# x_train, y_train, x_valid, y_valid = split_dataset_per_patient(ori_path, gt_path, sufix, removeStroma=False)

names = {i:x_valid[i].split('/')[-1][:-4] for i in range(len(x_valid))}


#######################################################################
############################### DATASET ###############################
#######################################################################


class Dataset(BaseDataset):
    """Read images, apply augmentation and preprocessing transformations.
    
    Args:
        images_dir (str): path to images folder
        masks_dir (str): path to segmentation masks folder
        class_values (list): values of classes to extract from segmentation mask
        augmentation (albumentations.Compose): data transfromation pipeline 
            (e.g. flip, scale, etc.)
        preprocessing (albumentations.Compose): data preprocessing 
            (e.g. noralization, shape manipulation, etc.)
    
    """
    
    CLASSES = ['all','none'] + classes_dataset 
    
    def __init__(
            self, 
            images_dir, 
            masks_dir, 
            classes=None, 
            augmentation=None, 
            preprocessing=None,
    ):
        self.images_fps = images_dir
        self.masks_fps = masks_dir
        
        # convert str names to class values on masks
        self.class_values = [self.CLASSES.index(cls.lower()) for cls in classes]
        self.augmentation = augmentation
        self.preprocessing = preprocessing
    
    def __getitem__(self, i):
        name = self.images_fps[i].split('/')[-1][:-4]
        
        # read data
        image = cv2.imread(self.images_fps[i])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mask = cv2.imread(self.masks_fps[i],-1)
        
        image = cv2.resize(image, (512,512))
        mask = cv2.resize(mask, (512,512), interpolation=cv2.INTER_NEAREST)

        # get the classes of each cell
        all_classes = np.zeros(mask.shape)
        with open(root+'Class/'+ name +'.class.csv', mode='r') as class_file:
            file = csv.reader(class_file, delimiter=',')
            mydict = dict((int(rows[0]),int(rows[1])) for rows in file)
        
        for i in mydict:
            all_classes[mask==i] = mydict[i]

        # labels used in the masks for each class, in the same order as CLASSES 
        ind2lab = [0, 0]+list(range(1,len(classes_dataset)+1,1))
        
        # extract from masks all labeled pixels or certain classes  
        if self.class_values[0] == 0 :
            classes = [(all_classes > 0)]
        else:
            classes = [(all_classes == ind2lab[v]) for v in self.class_values]
        mask = np.stack(classes, axis=-1).astype('float')
        
        # apply augmentations
        if self.augmentation:
            sample = self.augmentation(image=image, mask=mask)
            image, mask = sample['image'], sample['mask']
        
        # apply preprocessing
        if self.preprocessing:
            sample = self.preprocessing(image=image, mask=mask)
            image, mask = sample['image'], sample['mask']

        return image, mask
        
    def __len__(self):
        return len(self.images_fps)


#######################################################################
############################ AUGMENTATIONS ############################
#######################################################################

# choose data augmentation required
def get_training_augmentation(DAparams):
    train_transform = []
    if DAparams['flip']:
        flip = albu.HorizontalFlip(p=0.5)
        train_transform.append(flip)
    if DAparams['shift']:
        shift = albu.ShiftScaleRotate(scale_limit=0.1, rotate_limit=10, shift_limit=0.1, p=1, border_mode=0)
        train_transform.append(shift)

    return albu.Compose(train_transform)


def get_validation_augmentation():
    """Add paddings to make image shape divisible by 32"""
    test_transform = [
         ##albu.PadIfNeeded(384, 480)
    ]
    return albu.Compose(test_transform)


def to_tensor(x, **kwargs):
    return x.transpose(2, 0, 1).astype('float32')


def get_preprocessing(preprocessing_fn):
    """Construct preprocessing transform
    
    Args:
        preprocessing_fn (callbale): data normalization function 
            (can be specific for each pretrained neural network)
    Return:
        transform: albumentations.Compose
    
    """
    
    _transform = [
        albu.Lambda(image=preprocessing_fn),
        albu.Lambda(image=to_tensor, mask=to_tensor),
    ]
    return albu.Compose(_transform)


#######################################################################
####################### CREATE MODEL AND TRAIN ########################
#######################################################################

ENCODER = 'se_resnext50_32x4d'
ENCODER_WEIGHTS = 'imagenet'
DEVICE = 'cuda'
ACTIVATION = 'sigmoid'
CLASSES = classes_dataset

def train(params, params_names, num, metrics, model, train_dataset, valid_dataset):
    '''train a model {model}, with parameters {params}, model number {num}, using metrics {metrics}, 
    with train dataset {train_dataset} and validation dataset {valid_dataset}'''

    print('\n------------'+str(num)+'----------')
    parameters_line = 'epochs='+ str(params['epochs']) + \
    ', loss=' + str(params['loss']).split('(')[0] + ', lr=' + str(params['lr']) + ', opt=' \
    + str(params['optimizer']).split(' ')[0] + ', bs=' + str(params['batch_size'])
    print(parameters_line)

    #Final Logs
    train_logs_all = {'loss':[], 'fscore':[], 'recall':[], 'precision':[]} 
    valid_logs_all = {'loss':[], 'fscore':[], 'recall':[], 'precision':[]} 

    train_loader = DataLoader(train_dataset, batch_size=params['batch_size'], shuffle=True, num_workers=1)
    valid_loader = DataLoader(valid_dataset, 1, shuffle=False, num_workers=1) 

    # create epoch runners 
    # it is a simple loop of iterating over dataloader`s samples
    train_epoch = smp.utils.train.TrainEpoch(
      model, loss=params['loss'], metrics=metrics, optimizer=params['optimizer'], device=DEVICE, verbose=True)

    valid_epoch = smp.utils.train.ValidEpoch(
      model, loss=params['loss'], metrics=metrics, device=DEVICE, verbose=True)

    # train model for N epochs
    import re
    loss_name = str(params['loss']).split('(')[0]
    loss_name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', loss_name)
    loss_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', loss_name).lower()

    max_score = 0

    n = params['epochs']
    for i in range(0, n):
      
        print('\nEpoch: {}'.format(i))
        train_logs = train_epoch.run(train_loader)
        valid_logs = valid_epoch.run(valid_loader)

        train_logs_all['loss'].append(train_logs[loss_name])
        valid_logs_all['loss'].append(valid_logs[loss_name])
        train_logs_all['fscore'].append(train_logs['fscore'])
        valid_logs_all['fscore'].append(valid_logs['fscore'])
        train_logs_all['recall'].append(train_logs['recall'])
        valid_logs_all['recall'].append(valid_logs['recall'])
        train_logs_all['precision'].append(train_logs['precision'])
        valid_logs_all['precision'].append(valid_logs['precision'])
      
        # do something (save model, change lr, etc.)
        if max_score < valid_logs['fscore']:
            max_score = valid_logs['fscore']
            torch.save(model, output_path+'models/'+str(num)+'.best_model.pth')
            print('Model saved!')
  
  
    #Save results
    params['optimizer'] = ''
    params['loss'] =''
    data = {'params':params_names, 'training':train_logs_all, 'validation':valid_logs_all}

    with open(output_path +'logs/'+str(num)+'.'+parameters_line+'.txt', 'w') as outfile:
        json.dump(data, outfile)


def multiclass_metrics(pred, mask, results):
    ''' pred: prediction image
        mask: ground truth image
        results: container of results
    return: computes the confusion matrix of shape (classes+1)x(classes+1), computes the weighted metrics, mean metrics for class'''
    
    (mean_fscore, mean_prec, mean_rec, classes)=(0,0,0,0)
    confusion=np.zeros((len_classes+1,len_classes+1))

    for i in range(pred.shape[0]):
        for j in range(pred.shape[1]):
            mask_val = mask[i][j]
            pred_val = pred[i][j]
            confusion[int(pred_val)][int(mask_val)] += 1
    
    num_class = {i:0 for i in range(1,len_classes+1)}
    for i in range(1,len_classes+1):
        num_class[i] += sum(sum(mask==i))
    total = sum(num_class.values())
    num_class = {i:num_class[i]/total for i in num_class}
    
    (w_fscore, w_prec, w_rec)=(0,0,0)
    
    for k in range(1,len_classes+1):
        precision = confusion[k][k]/sum(confusion[k,:])
        recall = confusion[k][k]/sum(confusion[:,k])
        fscore = 2*precision*recall/(precision+recall)
        # print('Class', k,': fscore', round(fscore,6), 'precision', round(precision,6), 'recall', round(recall,6))
        if math.isnan(fscore):
            fscore=0
            precision=0
            recall=0
        results[k].append(fscore)
        w_fscore += fscore * num_class[k]
        w_prec += precision * num_class[k]
        w_rec += recall * num_class[k]

    # print('Weighted fscore', w_fscore, 'weighted precision', w_prec, 'weighted recall', w_rec)
    results['w_fscore'].append(w_fscore)
    results['w_prec'].append(w_prec)
    results['w_rec'].append(w_rec)
    return results

def modelToImages(model_num, valid_dataset, valid_dataset_vis, save=True):
    ''' model_num: number of the model
        valid_dataset: validation dataset
        valid_dataset_vis: validation dataset to obtain the name of the original images
        save: boolean to save or not save the images in a new folder
    return: retrieves the predicted image, computes the metrics and save the ground truth, original and predicted images'''
    
    model = torch.load(output_path + 'models/'+ str(model_num)+ '.best_model.pth')
    print(output_path+'models/'+str(model_num)+'.best_model.pth')
    if save:
        if not os.path.exists(output_path + 'images/'+str(model_num)):
            os.mkdir(output_path + 'images/'+str(model_num))
    
    results={i:[] for i in range(1,len_classes+1)}
    results['w_fscore']=[]
    results['w_prec']=[]
    results['w_rec']=[]
    total = len(valid_dataset)
    for i in range(total):
        name = valid_dataset_vis.images_fps[i].split('/')[-1][:-4]

        # print('Image ' + name )

        image_vis = valid_dataset_vis[i][0].astype('uint8')
        image, gt_mask= valid_dataset[i]

        gt_mask = gt_mask.squeeze()

        x_tensor = torch.from_numpy(image).to(DEVICE).unsqueeze(0)
        pr_mask = model.predict(x_tensor)
        pr_mask = pr_mask.squeeze().cpu().numpy()   #3x512x512 size 
        #assign to 1 the highest probability
        is_maximum =(pr_mask == pr_mask.max(axis=0))
        pr_mask = (pr_mask*is_maximum).round()
        
        #assign each pixel to its class and select it in 512x512 matrix
        if len(gt_mask.shape)>2:
            numcls=gt_mask.shape[0]
            for cls in range(0,numcls):
                gt_mask[cls,:,:] = gt_mask[cls,:,:]*(cls+1)
                pr_mask[cls,:,:] = pr_mask[cls,:,:]*(cls+1)
            gt_mask = np.amax(gt_mask,0)
            pr_mask = np.amax(pr_mask,0)
        
        results = multiclass_metrics(pr_mask, gt_mask, results)
        
        # visualize(
        #    original=image_vis,
        #    ground_truth=gt_mask, 
        #    predicted=pr_mask )
        
        if save:
            folder = 'images/' + str(model_num) + '/'
            image_write = cv2.cvtColor(image_vis, cv2.COLOR_RGB2BGR)
            cv2.imwrite(output_path + folder + str(i) +'.png', image_write)
            print('Original saved')
            cv2.imwrite(output_path + folder +  str(i) +'GT.png', gt_mask) 
            print('GT saved')
            cv2.imwrite(output_path + folder +  str(i) +'Pred.png', pr_mask) 
            print('Prediction saved')

    print('Mean fscore class 1-negative, Mean fscore class 2-high positive, Mean fscore class 3-mid positive, Mean fscore class 4-low positive, Mean fscore class 5-stroma')
    print('1:',round(np.mean(results[1]),6), '2:', round(np.mean(results[2]),6), '3:', round(np.mean(results[3]),6), '4:', round(np.mean(results[4]),6), '5:', round(np.mean(results[5]),6))
    print(round(np.mean(results['w_fscore']),6), round(np.mean(results['w_prec']),6), round(np.mean(results['w_rec']),6))


#######################################################################
#################### HYPERPARAMETER OPTIMIZATION ######################
#######################################################################

def hyperparameter_optimization(num, losses, learn_rates, optimizers, epochs, batch_sizes):
    ''' grid search for all the hyperparameters in each list of values: trains every combination of values and returns the metrics and images'''
    for loss in losses:
        for lr in learn_rates:
            for opt in optimizers:
                for N in epochs:
                    for b in batch_sizes:
                        # restart weights
                        print(len(CLASSES))
                        model = smp.Unet(encoder_name=ENCODER, encoder_weights=ENCODER_WEIGHTS, classes=len(CLASSES), activation=ACTIVATION,)
                        preprocessing_fn = smp.encoders.get_preprocessing_fn(ENCODER, ENCODER_WEIGHTS)
                        
                         #datasets
                        DA_params = {'flip':True, 'shift':True}
                        train_dataset = Dataset(x_train, y_train, augmentation=get_training_augmentation(DA_params), 
                                                preprocessing=get_preprocessing(preprocessing_fn), classes=CLASSES)

                        valid_dataset = Dataset(x_valid, y_valid, augmentation=get_validation_augmentation(), 
                                              preprocessing=get_preprocessing(preprocessing_fn), classes=CLASSES)
                        
                        metrics_ = [smp.utils.metrics.Fscore(threshold=0.5), smp.utils.metrics.Precision(threshold=0.5), 
                                    smp.utils.metrics.Recall(threshold=0.5)]

                        if loss == 'dice':
                            l = smp.utils.losses.DiceLoss()
                        else:
                            l = smp.losses.focal.FocalLoss(mode='multilabel')
                        
                        if opt == 'adam':
                            opt_ = torch.optim.Adam([dict(params=model.parameters(), lr=lr),])
                        else:
                            opt_ = torch.optim.SGD([dict(params=model.parameters(), lr=lr),])
                        

                        params = {'batch_size':b, 'optimizer': opt_, 'lr':lr, 'loss':l, 'epochs': N }
                        params_names = {'batch_size':b, 'optimizer': opt, 'lr':lr, 'loss':loss, 'epochs': N}
                        train(params, params_names, str(num), metrics_, model, train_dataset, valid_dataset)
                        
                        valid_dataset_vis = Dataset(x_valid, y_valid, classes=CLASSES)
                        modelToImages(str(num), valid_dataset, valid_dataset_vis, save=False)
                        print(loss,lr,opt,N,b)
                        # logs_graphic(output_path+'logs', str(num))
                        
                        num=num+1


#######################################################################
################### OPTIMIZATION HYPERPARAMETERS ######################
#######################################################################

num_model= 9

# #Loss
# diceLoss = smp.utils.losses.DiceLoss()
# focalLoss = smp.losses.focal.FocalLoss(mode='multilabel')
# losses = [diceLoss]
losses = ['dice']

#Hyperparameters

#Learning Rate
learn_rates = [0.005]

#Optimizer
optimizers = ['adam']

#Epochs
epochs=[100]

#Batch Size
batch_sizes = [4]

hyperparameter_optimization(num_model, losses, learn_rates, optimizers, epochs, batch_sizes)
