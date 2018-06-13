import os
import cv2
import numpy as np
import math

def changeclass(x, y, img, class_now, class_target):
    #Find the top and down coordinate
    while img[x, y] == class_now:
        y0 = y
        img[x, y] = class_target
        y += 1
    y_end = y
    y = y0
    while img[x, y] == class_now:
        img[x, y] = class_target
        y -= 1
    y_start = y

    while img[x, y] == class_now:
        x0 = x
        img[x, y] = class_target
        x += 1
    x_end = y
    x = x0

    while img[x, y] == class_now:
        img[x, y] = class_target
        x -= 1
    x_start = x
    #Search the pixels from (x0, y0) in 8 directions
    x = x0
    while x in range(x_start, x_end):
        if img[x, y_start + 1] == class_now:
            if img[x, y_end + 1] == class_now:
                img[x, y_start + 1:y_end + 1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start + 1:y_end] = class_target
            else:
                img[x, y_start + 1:y_end - 1] = class_target
                y_end -= 1
            y_start += 1
        elif img[x, y_start] == class_now:
            if img[x, y_end + 1] == class_now:
                img[x, y_start:y_end + 1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start:y_end] = class_target
            else:
                img[x, y_start:y_end - 1] = class_target
                y_end -= 1
        else:
            if img[x, y_end+1] == class_now:
                img[x, y_start-1:y_end+1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start-1:y_end] =class_target
            else:
                img[x, y_start-1:y_end-1] = class_target
                y_end -= 1
            y_start -= 1
        x += 1
    x = x0
    while x in range(x_start, x_end):
        if img[x, y_start + 1] == class_now:
            if img[x, y_end + 1] == class_now:
                img[x, y_start + 1:y_end + 1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start + 1:y_end] = class_target
            else:
                img[x, y_start + 1:y_end - 1] = class_target
                y_end -= 1
            y_start += 1
        elif img[x, y_start] == class_now:
            if img[x, y_end + 1] == class_now:
                img[x, y_start:y_end + 1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start:y_end] = class_target
            else:
                img[x, y_start:y_end - 1] = class_target
                y_end -= 1
        else:
            if img[x, y_end+1] == class_now:
                img[x, y_start-1:y_end+1] = class_target
                y_end += 1
            elif img[x, y_end] == class_now:
                img[x, y_start-1:y_end] =class_target
            else:
                img[x, y_start-1:y_end-1] = class_target
                y_end -= 1
            y_start -= 1
        x -= 1
    return img

def searchcircle(x, y, radiu, img, class_num):
    #Find a node that belongs to the class in the image, and return the coordinate of the node.
    #Range is used for controling the search speed.
    sz1 = img.shape[0]
    sz2 = img.shape[1]
    for i in range(sz1):
        for j in range(sz2):
            if (i-x)**2 + (j-y)**2 <= radiu**2:
                if img[i, j] == class_num:
                    return i, j
            else:
                continue
#Search the file dict
def search(coordinate1, coordinate2, img):
    x1 = coordinate1[0]
    y1 = coordinate1[1]
    x2 = coordinate2[0]
    y2 = coordinate2[1]
    #Find the left ankle
    #1, Search the nearest left shoe (class 18) pixel
    class_num = 18
    range = 100
    x3, y3 = searchcircle(x1, y1, range, img, class_num)
    x4, y4 = searchcircle(x2, y2, range, img, class_num)
    if dist(x3, y3, x1, x2) < dist(x4, y4, x1, y1):
        img_new = changeclass(x3, y3, img, class_now=18, class_target=19)
    else:
        img_new = changeclass(x4, y4, img, class_now=18, class_target=19)
    return(img_new)

def search_shoe(joint_array, joint_dict, image, img):
    #print(joint_array, joint_dict,image)
    index = joint_dict.index(image)
    #print(index)
    co_left_ankle = [joint_array[index, 22], joint_array[index, 23]]
    co_right_ankle = [joint_array[index, 16], joint_array[index, 17]]
    #Search algorithmn
    img_new = search(co_left_ankle, co_right_ankle, img)
    return img_new

def search_leg(joint_array, joint_dict, image, img):
    index = joint_dict.find(image)
    co_left_knee = [joint_array[index, 20], joint_array[index, 21]]
    co_right_knee = [joint_array[index, 14], joint_array[index, 15]]
    co_left_ankle = [joint_array[index, 22], joint_array[index, 23]]
    co_right_ankle = [joint_array[index, 16], joint_array[index, 17]]
    #Find the line between the two nodes
    x_left = list(range(co_left_knee[0], co_left_ankle[0], 1))
    y_left = line_2nodes(co_left_knee[0], co_left_knee[1], co_left_ankle[0], co_left_ankle[1], x_left)
    x_right = list(range(co_right_knee[0], co_right_ankle[0], 1))
    y_right = line_2nodes(co_right_knee[0], co_right_knee[1], co_right_ankle[0], co_right_ankle[1], x_right)
    #Search algorithmn
    img_new = searchline(x_left, y_left, img, class_now=17, class_target=16)
    img_new = searchline(x_right, y_right, img_new, class_now=16, class_target=17)
    return img_new

def search_arm_down(joint_array, joint_dict, image, img):
    index = str(joint_dict).find(image)
    co_left_elbow = [joint_array[index, 8], joint_array[index, 9]]
    co_right_elbow = [joint_array[index, 2], joint_array[index, 3]]
    co_left_wrist = [joint_array[index, 10], joint_array[index, 11]]
    co_right_wrist = [joint_array[index, 4], joint_array[index, 5]]
    # Find the line between the two nodes
    x_left = list(range(co_left_elbow[0], co_left_wrist[0], 1))
    y_left = line_2nodes(co_left_elbow[0], co_left_elbow[1], co_left_wrist[0], co_left_wrist[1], x_left)
    x_right = list(range(co_right_elbow[0], co_right_wrist[0], 1))
    y_right = line_2nodes(co_right_elbow[0], co_right_elbow[1], co_right_wrist[0], co_right_wrist[1], x_right)
    # Search algorithmn
    img_new = searchline(x_left, y_left, img, class_now=17, class_target=16)
    img_new = searchline(x_right, y_right, img_new, class_now=16, class_target=17)
    return img_new

def search_arm_up(joint_array, joint_dict, image, img):
    index = str(joint_dict).find(image)
    co_left_elbow = [joint_array[index, 8], joint_array[index, 9]]
    co_right_elbow = [joint_array[index, 2], joint_array[index, 3]]
    co_left_shoulder = [joint_array[index, 6], joint_array[index, 7]]
    co_right_shoulder = [joint_array[index, 0], joint_array[index, 1]]
    # Find the line between the two nodes
    x_left = list(range(co_left_elbow[0], co_left_shoulder[0], 1))
    y_left = line_2nodes(co_left_elbow[0], co_left_elbow[1], co_left_shoulder[0], co_left_shoulder[1], x_left)
    x_right = list(range(co_right_elbow[0], co_right_shoulder[0], 1))
    y_right = line_2nodes(co_right_elbow[0], co_right_elbow[1], co_right_shoulder[0], co_right_shoulder[1], x_right)
    # Search algorithmn
    img_new = searchline(x_left, y_left, img, class_now=17, class_target=16)
    img_new = searchline(x_right, y_right, img_new, class_now=16, class_target=17)
    return img_new

def searchline(x, y, img, class_now, class_target):
    #x, y are list of coordinates on the line that through the knee and ankle nodes
    img_new = img
    parameter = 0
    for i in range(y):
        while(img_new[x[i+parameter], y[i]] == class_now):
            parameter += 1
        parameter_up = parameter
        while(img_new[x[i+parameter], y[i]] == class_now):
            parameter -= 1
        parameter_down = parameter
        img_new[x[parameter_down:parameter_up], y[i]] = class_target
    return img_new

def line_2nodes(x1, y1, x2, y2, x):
    k = (y2-y1)/(x2-x1)
    y = k*(x-x1)+y1
    return y

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#1, Read joint info
jointfile_path = 'E:/Workplace/LIPDataset/pose/test0/'
jointfile = os.listdir(jointfile_path)
joint_dict = []
joint_array = np.empty((10000, 32))
index_x = 0
for joint in jointfile:
    joint_dict.append(str(joint).split('.')[0])
    #print(joint)
    with open(jointfile_path + joint, 'r') as f:
        data = f.readlines()
        for line in data:
            coordinate = line.split()
            joint_array[index_x, :] = coordinate
            index_x += 1
#print(joint_dict)
#print(joint_array)

#2, Read Image
rootpath = 'E:/Workplace/LIPDataset/pose/results0/'
path = os.listdir(rootpath)
#Main function
for image in path:
    #print(image)
    img = cv2.imread(rootpath + image)
    #print(img)
    sz = img.shape
    sz1 = sz[0]  # height
    sz2 = sz[1]  # width
    sz3 = sz[2]  # if is RGB
    img = img[:, :, 2]
    image_para = image
    image_para = str(image_para.split('.')[0])
    #print(image)
    image_new1 = search_shoe(joint_array, joint_dict, image_para, img)
    image_new2 = search_leg(joint_array, joint_dict, image_para, image_new1)
    image_new3 = search_arm_down(joint_array, joint_dict, image_para, image_new2)
    image_new4 = search_arm_up(joint_array, joint_dict, image_para, image_new3)
    image[:, :, 1] = image_new4
    image[:, :, 2] = image_new4
    image[:, :, 3] = image_new4

