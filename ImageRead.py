import cv2
import glob as gb

img_path_validation = gb.glob(r'E:\Workplace\LIPDataset\TrainVal_images\TrainVal_images\val_images\*jpg')
img_path_validation_label = gb.glob(r'E:\Workplace\LIPDataset\TrainVal_parsing_annotations\TrainVal_parsing_annotations\val_segmentations\*png')
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

f_validation = open('E:\Workplace\LIPDataset\Validation.txt', 'w')
for i in range(index):
    print(i)
    print(sz2[i])
    print(PathValidation[i])
    print(PathValLabel[i])
    f_validation.write('{"dbInfo": {"frameID": -1, "vID": "ADE20k"}, "width":' + str(sz2[i]) +
        ', "fpath_img" : "' + PathValidation[i] + '" ,' + '"ade_scene"' +
        ':' + 'N/A' + ',' + '"height":' + str(sz1[i]) + ',' + 'dbName' + ':' + '"ADE20k":' + '"fpath_segm": "' + PathValLabel[i] + '"}\n')
f_validation.close()
