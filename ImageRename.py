import os

path = 'E:/Workplace/LIPDataset/Train_parsing_reversed_labels/train_segmentations_reversed/'
img_name = os.listdir(path)
print(img_name)
for img in img_name:
    new_name = 'R' + img
    os.rename(path + str(img), path + str(new_name))