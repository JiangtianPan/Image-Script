import glob as gb
import cv2

root_path = 'E:/Workplace/LIPDataset/TrainVal_images/TrainVal_images'
img_path_train = gb.glob(root_path + '/Train_images/*jpg')
img_path_validation = gb.glob(root_path + '/val_images/*jpg')

for path_train in img_path_train:
    img_train = cv2.imread(path_train)
    img_train = cv2.flip(img_train, 1)
    path_train = str(path_train.strip('/').split('/')[-1])
    position = path_train.index('_')
    path_train = path_train[position+8:len(path_train)]
    path_train = "R" + path_train
    print(path_train)
    cv2.imwrite(root_path + "/Train_reversed/" + path_train, img_train, None)

for path_validation in img_path_validation:
    img_valiation = cv2.imread(path_validation)
    img_valiation = cv2.flip(img_valiation, 1)
    path_validation = str(path_validation.strip('/').split('/')[-1])
    position = path_validation.index('_')
    path_validation = path_validation[position+8:len(path_validation)]
    path_validation = "R" + path_validation
    print(path_validation)
    cv2.imwrite(root_path + "/val_reversed/" + path_validation, img_valiation, None)


