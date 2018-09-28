import os
import numpy as np
#from scipy import misc
#from PIL import Image
import cv2
#from libtiff import TIFF 
"""
def patch_move(start, step):
    start = start + step
    return start
"""
def patch_sample(image, start_x, start_y, step_x, step_y, patch_height, patch_width):
    height = image.shape[0]
    width = image.shape[1]
    #print(height, width)
    end_x = start_x + patch_height - 1
    end_y = start_y + patch_width - 1
    #print(end_x, end_y)
    if end_x <= height and end_y <= width:
        startX, startY = start_x, start_y
        print('1')
    if end_x > height:
        startX, startY = height - patch_height, start_y
        print('2')
    if end_y > width:
        startX, startY = start_x, width - patch_width
        print('3')
    if end_x > width and end_y > height:
        startX, startY = height - patch_height, width - patch_width
    print(startY, patch_width)
    patch = image[startX : (startX + patch_height - 1), startY : (startY + patch_width - 1)]
    return patch


end_x, end_y = 7500, 11500
min_overlap_rate = 0.1
patch_height = 448
patch_width = 448
step_x = int((1 - min_overlap_rate) * patch_height)
step_y = int((1 - min_overlap_rate) * patch_width)
root = 'G:/Document/GDA/5-Toronto (ALS, LiDAR_DSM)/Images/'
tiflist = os.listdir(root)
for files in tiflist:
    if os.path.splitext(files)[-1] == '.tif':
        image = cv2.imread(root + files, -1)
        #cv2.imwrite(root + 'txt' + files, image)
        #print(image)
        height = image.shape[0]
        width = image.shape[1]
        #print(height, width)
        #print(start_x, start_y)
        count_x, count_y = 0, 0
        start_x, start_y = 0, 0
        while start_x < height:
            while start_y < width:
                patch = patch_sample(image, start_x, start_y, step_x, step_y, patch_height, patch_width)
                print(patch.shape)
                print('X:' + str(count_x), 'Y:' + str(count_y))
                cv2.imwrite(root + str(count_x) + '_' + str(count_y) + '_' + files, patch)
                start_y += step_y
                count_y += 1
            count_y = 0
            start_y = 0
            start_x += step_x
            count_x += 1
            
    

