import numpy as np
import cv2
import glob as gb
import codecs
import os
file_path = 'E:/Workplace/LIPDataset/393_results_person/'
img_path = 'E:/Workplace/LIPDataset/Testing_multi/'
#Matrix =[]
#Matrix = np.arange(2094).reshape
def imgSeg(x1, y1, x2, y2, img):
    sz = img.shape
    sz1 = sz[0]
    sz2 = sz[1]

    if x1<0:
        x1 =0
    elif x1>sz2:
        x1 = sz2
    elif y1<0:
        y1 = 0
    elif y1>sz1:
        y1 = sz1
    elif x2<0:
        x2 = 0
    elif x2>sz2:
        x2 = sz2
    elif y2<0:
        y2 = 0
    elif y2>sz1:
        y2 = sz1

    img_new = img[y1:y2, x1:x2, :]
    return img_new
"""
#Conbine all information into one txt file
os.chdir(file_path)
files = gb.glob('*.txt')
print(files)
all = codecs.open('all.txt', 'a')
#print(all)
for file in files:
    if os.path.getsize(file) == 0:
        continue
    f = open(file)
    print(f)
    #lines = f.readline()
    #print(lines)
    for lines in f:
        print(lines)
        all.write(file.strip('.txt') + ' ' + lines)
    f.close()
"""

#Read the 'all' file
i = 0
line_reserve = [[0]]
line_bbox = []
S_reserve = 0
S_bbox = 0
all = open(file_path + 'all.txt')
for line in all:
    line = line.strip('\n')
    line = line.split(' ')
    #print(line)
    img = cv2.imread(line[0] +  '.jpg')
    x1 = round(float((line[1])))
    y1 = round(float((line[2])))
    x2 = round(float((line[3])))
    y2 = round(float((line[4])))
    #print(x1,y1,x2,y2)
    cv2.rectangle(img, (x1, y1), (x2, y2), color=(0,255,0))
    cv2.imwrite(line[0] + '.jpg', img)
    S = (x2 - x1) * (y2 - y1)
    if line[0] == line_reserve[0]:
        #print(line_reserve)
        if S < S_reserve:
            #保留S_reserve的bbox
            S_bbox = S_reserve
            continue
            #line_bbox.append(line_reserve)
        elif S > S_reserve:
            #保留S的bbox
            #S_bbox = S
            #line_bbox.append(line)
            line_reserve = line
            S_reserve = S
            continue
        else:
            continue
    line_bbox.append(line_reserve)
    line_reserve = line
    S_reserve = S
    #print(line_reserve, S_reserve)
    #print(line_bbox, S_bbox)
line_bbox = line_bbox[1:len(line_bbox)]

print(line_bbox)
imageSeg = codecs.open('imageSeg.txt', 'a')
for index in line_bbox:
    print(index)
    imageSeg.write(str(index))
    print(index[0])
    image = cv2.imread(img_path + index[0] + '.jpg')
    #cv2.imshow('a',image)
    cv2.waitKey()
    x1 = index[1]
    y1 = index[2]
    x2 = index[3]
    y2 = index[4]
    image_new = imgSeg(int(x1), int(y1), int(x2), int(y2), image)
    cv2.imwrite(index[0] + '_seg' + '.jpg', image_new)











