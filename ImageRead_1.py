import operator
import glob as gb
import cv2
import re
import os


# Returns a list of all folders with participant numbers
img_path_train = gb.glob(r'E:/Workplace/LIPDataset/TrainVal_images/TrainVal_images/Train_reversed/*jpg')
#img_path_train = gb.glob(r'/export/home/pjt/LIPData/TrainVal_images/train_reversed/*jpg')
img_path_label = gb.glob(r'E:/Workplace/LIPDataset/Train_parsing_reversed_labels/train_segmentations_reversed/*png')
#img_path_label = gb.glob(r'/export/home/pjt/LIPData/Train_parsing_reversed_labels/train_segmentations_reversed/*png')

PathTrain = []
PathLabel = []
sz1 = []
sz2 = []
sz3 = []
#for path_train, path_label in img_path_train, img_path_label:
for path_train in img_path_train:
    img_train = cv2.imread(path_train)
    PathTrain.append(path_train)
    path_train = str(path_train.strip('/').split('/')[-1])
    path_train = re.sub("\D", " ", path_train)
    path_train = path_train.strip()
    path_train = re.sub("\D", "_", path_train)
    path_train = 'E:/Workplace/LIPDataset/Train_parsing_reversed_labels/train_segmentations_reversed/'+ path_train + '.png'
    PathLabel.append(str(path_train))
    #print(path_train)

    shape_train = img_train.shape

    sz1.append(shape_train[0])  # height(rows) of image
    sz2.append(shape_train[1])  # width(colums) of image
    #sz3.append(shape_train[2])  # the pixels value is made up of three primary colors
"""
for path_label in img_path_label:
    img_label = cv2.imread(path_label)
    #print(path_label)
    PathLabel.append(path_label)
"""
index = len(PathTrain)
#print(sz1)
#print(PathTrain)
#print(PathLabel)

#f = open('/export/home/pjt/LIPData/semantic-segmentation-pytorch/data/Train.txt', 'a')
number = 0
for i in range(index):

    print(PathLabel[i])
    print(PathTrain[i])
"""
    f.write('{"dbInfo": {"frameID": -1, "vID": "ADE20k"}, "width":' + str(sz2[i]) + ', "fpath_img": "' + PathTrain[i] + '", ' + '"ade_scene"' + ':' + ' "abbey"' + ', ' + ' "height": ' + str(sz1[i]) + ', ' + '"dbName"' + ': ' + '"ADE20k", ' + '"fpath_segm": "' + PathLabel[i] + '"}\n')
f.close()
"""
"""
img_path_validation = gb.glob(r'/export/home/pjt/LIPData/TrainVal_images/val_images/*jpg')
img_path_validation_label = gb.glob(r'/export/home/pjt/LIPData/TrainVal_parsing_annotations/val_segmentations/*png')
PathValidation = []
PathValLabel = []
sz1 = []
sz2 = []
sz3 = []

for path_validation in img_path_validation:
    # path_train, path_label = path
    img_validation = cv2.imread(path_validation)
    PathValidation.append(path_validation)
    #cv2.imshow('img', img)
    #cv2.waitKey(1000)
    shape_validation = img_validation.shape
    #print(shape_train)
    sz1.append(shape_validation[0])  # height(rows) of image
    sz2.append(shape_validation[1])  # width(colums) of image
    sz3.append(shape_validation[2])  # the pixels value is made up of three primary colors

for path_validation_label in img_path_validation_label:
    img_validation_label = cv2.imread(path_validation_label)
    PathValLabel.append(path_validation_label)

index = len(PathValidation)
print(sz1)
print(PathValidation)
print(PathValLabel)

f = open('/export/home/pjt/LIPData/semantic-segmentation-pytorch/data/validation.txt', 'a')
for i in range(index):
    print(i)
    print(sz2[i])
    print(PathValidation[i])
    print(PathValLabel[i])
    f.write('{"dbInfo": {"frameID": -1, "vID": "ADE20k"}, "width":' + str(sz2[i]) +
        ', "fpath_img": "' + PathValidation[i] + '", ' + '"ade_scene"' +
        ':' + ' "abbey"' + ', ' + ' "height": ' + str(sz1[i]) + ', ' + '"dbName"' + ': ' + '"ADE20k", ' + '"fpath_segm": "' + PathValLabel[i] + '"}\n')
f.close()
"""
