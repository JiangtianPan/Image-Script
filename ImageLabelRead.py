import os
#import os.path
def ImageList(rootdir, path, args):
    rootdir = "E:/Workplace/LIPDataset/Testing_images/"
    path = "E:/Workplace/LIPDataset/Testing_images/testing_images/"
    test_img = []
    file = open(rootdir + 'test_id.txt', 'r')
    #line = file.readline()
    #print(line)
    for line in file:
        line = line.strip('\n')
        test_img.append(path + line + '.jpg')
    #print(test_img)

    return test_img
