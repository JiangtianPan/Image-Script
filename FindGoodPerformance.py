import cv2
import os

file_path = 'E:/Workplace/LIPDataset/393_results_person/'
img_path = 'E:/Workplace/semantic-segmentation-pytorch-master/good_performance/'
target_pah = 'E:/Workplace/LIPDataset/393_results_person/'
#result = []
file1 = open(file_path + 'good_performance.txt')
print(file1)
file2 = open(target_pah + 'principle_component.txt')
file = open(file_path + 'result.txt', 'a')
for line1 in file1:
    line1 = str(line1).strip('\n')
    for line2 in file2:
        line2 = line2.strip('\n')
        line2 = line2.split(',')
        print(line1)
        print(line2[0])
        if line1 == line2[0]:
            line1 = line2
            file.write(line1 + '\n')
file.close()

"""
    #print(line[0])
    if os.path.exists(img_path + line[0] + '.jpg') is True:
        #print(os.path.exists(img_path + line[0] + '.jpg'))
        result.append(line[0])
print(result)
"""