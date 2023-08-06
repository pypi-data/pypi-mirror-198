# Install required libs
import os
import torch
import numpy as np
from torch.utils.data import DataLoader
from  torch.utils.data import Dataset as BaseDataset
from scipy.ndimage import gaussian_filter
import scipy.ndimage as ndimage

import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
import functions.segmentation_models_pytorch as smp
import albumentations as albu

from functions.utils import *

#######################################################################
############################## LOAD DATA ##############################
#######################################################################

output_path = './results/count/'
create_subfolders_output(output_path, ['models', 'logs', 'images'])

from parameters import *

##########TO CHANGE ##############

# RE
root = root_directory_re
classes_dataset = classes_re
classes_names = classes_names_re

# KI67 
# root = root_directory_ki67#_v2
# classes_dataset = classes_ki67
# classes_names = classes_names_ki67

len_classes = len(classes_dataset)

ori_path = root + 'Images/'
gt_path = root + 'Points/'
sufix = '.points'

# split randomly (80-20)
x_train, y_train, x_valid, y_valid = split_dataset(ori_path, gt_path, sufix)

#split per patients (option: removing 2 images with only stroma)
# x_train, y_train, x_valid, y_valid = split_dataset_per_patient(ori_path, gt_path, sufix, removeStroma=True)

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
    
    CLASSES = ['cell']
    
    def __init__(
            self, 
            images_dir, 
            masks_dir, 
            sigma_,
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
        self.sigma = sigma_
    
    def __getitem__(self, i):
        name = self.images_fps[i].split('/')[-1][:-4]
        
        # read data
        image = cv2.imread(self.images_fps[i])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (512,512))

        mask = cv2.imread(self.masks_fps[i], 0)
        mask = mask/255
        
        mask = gaussian_filter(mask, sigma=self.sigma)
        mask = mask/mask.max()
        mask = cv2.resize(mask, (512,512), interpolation=cv2.INTER_NEAREST) 
   
        # extract certain classes from mask 
        mask = np.stack([mask], axis=-1).astype('float')
        
        # apply augmentations
        if self.augmentation:
            sample = self.augmentation(image=image, image1=mask)
            image, mask = sample['image'], sample['image1']
        
        # apply preprocessing
        if self.preprocessing:
            sample = self.preprocessing(image=image, mask=mask)
            image, mask = sample['image'], sample['mask']

        return image, mask
        
    def __len__(self):
        return len(self.images_fps)
    
    def name(self, i):
        return self.images_fps[i].split('/')[-1][:-4]


#######################################################################
############################ AUGMENTATIONS ############################
#######################################################################

def get_training_augmentation(DAparams):       
    train_transform = []
    if DAparams['flip']:
        flip = albu.HorizontalFlip(p=0.5)
        train_transform.append(flip)
    if DAparams['shift']:
        shift = albu.ShiftScaleRotate(scale_limit=0.1, rotate_limit=10, shift_limit=0.2, p=1, border_mode=0)
        train_transform.append(shift)
    if DAparams['bright']:
        # bright =  albu.OneOf([albu.CLAHE(p=1),albu.RandomBrightness(p=1),albu.RandomGamma(p=1),], p=0.0,)
        # train_transform.append(bright)
        pass
    if DAparams['blur']:
        # blur = albu.OneOf([albu.IAASharpen(p=1),albu.Blur(blur_limit=3, p=1),albu.MotionBlur(blur_limit=3, p=1),],p=0.0,)
        # train_transform.append(blur)
        pass
    if DAparams['contrast']:
        # contrast = albu.OneOf([albu.RandomContrast(p=1), albu.HueSaturationValue(p=1),], p=0.0,)
        # train_transform.append(contrast)
        pass

    return albu.Compose(train_transform, additional_targets= {'image':'image','image1':'image'} )


def get_validation_augmentation():
    """Add paddings to make image shape divisible by 32"""
    test_transform = [
         ##albu.PadIfNeeded(384, 480)
    ]
    return albu.Compose(test_transform, additional_targets= {'image':'image','image1':'image'} )


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
    return albu.Compose(_transform, additional_targets= {'image':'image','image1':'image'}) 


#######################################################################
####################### CREATE MODEL AND TRAIN ########################
#######################################################################

ENCODER = 'se_resnext50_32x4d'
ENCODER_WEIGHTS = 'imagenet'
DEVICE = 'cuda'
ACTIVATION = 'sigmoid'
CLASSES = ['cell']

def train(params, params_names, num, metrics_, model, train_dataset, valid_dataset):
    print('\n------------'+str(num)+'----------')
    parameters_line = 'Thresh='+str(params['thresh']) + ', sigma='+ str(params['sigma']) + ', epochs='+ str(params['epochs']) + \
    ', loss=' + str(params['loss']).split('(')[0] + ', lr=' + str(params['lr']) + ', opt=' \
    + str(params['optimizer']).split(' ')[0] + ', bs=' + str(params['batch_size'])
    print(parameters_line)

    #Final Logs
    train_logs_all = {'loss':[],'fscore':[], 'recall':[], 'precision':[]} 
    valid_logs_all = {'loss':[],'fscore':[], 'recall':[], 'precision':[]} 

    train_loader = DataLoader(train_dataset, batch_size=params['batch_size'], shuffle=True, num_workers=1)
    valid_loader = DataLoader(valid_dataset, batch_size=1, shuffle=False, num_workers=1) 

    # create epoch runners 
    # it is a simple loop of iterating over dataloader`s samples
    train_epoch = smp.utils.train.TrainEpoch(
      model, loss=params['loss'], metrics=metrics_, optimizer=params['optimizer'], device=DEVICE, verbose=True)

    valid_epoch = smp.utils.train.ValidEpoch(
      model, loss=params['loss'], metrics=metrics_, device=DEVICE, verbose=True)

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
        train_logs_all['fscore'].append(train_logs['custom_fscore'])
        valid_logs_all['fscore'].append(valid_logs['custom_fscore'])
        train_logs_all['recall'].append(train_logs['custom_recall'])
        valid_logs_all['recall'].append(valid_logs['custom_recall'])
        train_logs_all['precision'].append(train_logs['custom_precision'])
        valid_logs_all['precision'].append(valid_logs['custom_precision'])

        # do something (save model, change lr, etc.)
        if max_score < valid_logs['custom_fscore']:
            max_score = valid_logs['custom_fscore']
            torch.save(model, output_path+'models/'+str(num)+'.best_model.pth')
            print('Model saved!')

    #Save results
    params['optimizer'] = ''
    params['loss'] = ''
    data = {'params':params_names, 'training':train_logs_all, 'validation':valid_logs_all}

    #change the number at each test
    with open(output_path +'logs/'+str(num)+'.'+parameters_line+'.txt', 'w') as outfile:
        json.dump(data, outfile)
    print('Model saved as'+ str(num)+'.'+parameters_line+'.txt')


def modelToImages(model_num, valid_dataset, valid_dataset_vis, th, new_name=None, save=True):
    ''' model_num: number of the model
        valid_dataset: validation dataset
        valid_dataset_vis: validation dataset to obtain the name of the original images
        save: boolean to save or not save the images in a new folder
    return: retrieves the predicted image, computes the metrics and save the ground truth, original and predicted images'''

    model = torch.load(output_path + 'models/'+ str(model_num)+ '.best_model.pth')
    model.eval()
    print(output_path+'models/'+str(model_num)+'.best_model.pth')
    if new_name == None:
        new_name = model_num
    if save:
        if not os.path.exists(output_path+'images/'+str(new_name)):
            os.mkdir(output_path+'images/'+str(new_name))

    total = len(valid_dataset)
    (sum_fscores, sum_precs, sum_recs)=(0,0,0)
    for i in range(total):
        name = valid_dataset_vis.images_fps[i].split('/')[-1][:-4]

        # print('Image ' + name )

        image_vis = valid_dataset_vis[i][0].astype('uint8')
        image, gt_mask= valid_dataset[i]

        gt_mask = gt_mask.squeeze()

        x_tensor = torch.from_numpy(image).to(DEVICE).unsqueeze(0)
        pr_mask = model.predict(x_tensor)
        pr_mask = pr_mask.squeeze().cpu().numpy()

        maxims_pr, lst_pr = smp.utils.new_metrics.find_local_maxima(pr_mask, th)
        maxims_gt, lst_gt = smp.utils.new_metrics.find_local_maxima(gt_mask, th)
        
        prec,rec, fscore = smp.utils.new_metrics.compare_binary(lst_pr, lst_gt)
        # print('Precision', prec, 'Recall', rec, 'Fscore', fscore)

        sum_fscores += fscore
        sum_precs += prec
        sum_recs += rec
#         visualize(
#             image=image_vis, 
#             ground_truth_mask=maxims_gt, 
#             predicted_mask=pr_mask,
#             centroides = maxims_pr
#         )
        
        if save:
            folder = 'images/' + str(new_name) + '/'

            image_write = cv2.cvtColor(image_vis, cv2.COLOR_RGB2BGR)
            cv2.imwrite(output_path + folder + str(i) +'.png', image_write)
            print('Original saved')

            cv2.imwrite(output_path + folder +  str(i) +'GT.png', maxims_gt)
            print('GT saved')

            cv2.imwrite(output_path + folder + str(i) + 'Centr.png', maxims_pr)
            print('Centroides saved')

    print('fscore='+str(sum_fscores/total)+', precision='+str(sum_precs/total)+', recall='+str(sum_recs/total))


#######################################################################
#################### HYPERPARAMETER OPTIMIZATION ######################
#######################################################################

def hyperparameter_optimization(num, losses, learn_rates, optimizers, epochs, batch_sizes, thresholds, sigmes):
    for loss in losses:
        for lr in learn_rates:
            for opt in optimizers:
                for N in epochs:
                    for b in batch_sizes:
                        for s in sigmes:
                            for th in thresholds:
                                # restart weights
                                model = smp.Unet(encoder_name=ENCODER, encoder_weights=ENCODER_WEIGHTS, classes=len(CLASSES), activation=ACTIVATION,)
                                preprocessing_fn = smp.encoders.get_preprocessing_fn(ENCODER, ENCODER_WEIGHTS)

                                #datasets
                                train_dataset = Dataset(x_train, y_train, s, augmentation=get_training_augmentation({'shift':True, 'flip':True, 'bright':False, 'blur':False, 'contrast':False}), 
                                                        preprocessing=get_preprocessing(preprocessing_fn), classes=CLASSES)

                                valid_dataset = Dataset(x_valid, y_valid, s, augmentation=get_validation_augmentation(), 
                                                      preprocessing=get_preprocessing(preprocessing_fn), classes=CLASSES)

                                #metrics
                                if loss == 'mse':
                                    l = smp.utils.losses.MSELoss()
                                else:
                                    print('LOSS IS NONE')
                                    l = None
                                
                                metrics_ = [smp.utils.metrics.CustomAll(threshold=th)]

                                #optimizer
                                if opt == 'adam':
                                    opt_ = torch.optim.Adam([dict(params=model.parameters(), lr=lr),])
                                else:
                                    opt_ = torch.optim.SGD([dict(params=model.parameters(), lr=lr),])


                                params = {'thresh': th, 'sigma': s, 'batch_size':b,  'optimizer': opt_, 'lr':lr, 'loss':l, 'epochs': N}
                                params_names = {'thresh': th, 'sigma': s, 'batch_size':b, 'optimizer': opt, 'lr':lr, 'loss':loss, 'epochs': N }
                                train(params, params_names, str(num), metrics_, model, train_dataset,valid_dataset)
                            
                                valid_dataset_vis = Dataset(x_valid, y_valid, classes=CLASSES, sigma_=s)
                                
                                modelToImages(str(num), valid_dataset, valid_dataset_vis,th, save=False)
                                
                                # logs_graphic(output_path+'logs', str(num))

                                num=num+1


#######################################################################
################### OPTIMIZATION HYPERPARAMETERS ######################
#######################################################################

#Hyperparameters

num_model = 0

#Loss
# losses = [smp.utils.losses.MSELoss()]
losses = ['mse']

#Threshold metrics
thresholds = [0.15]

sigmes = [6] 

#Learning Rate
#learn_rates = [0.05,0.005,0.0005,0.00005]
learn_rates = [0.0005]

#Optimizer
optimizers = ['adam']

#Epochs
epochs = [100]

#Batch Size
batch_sizes = [4]

#write name for the combination
hyperparameter_optimization(num_model, losses, learn_rates, optimizers, epochs, batch_sizes, thresholds, sigmes)
