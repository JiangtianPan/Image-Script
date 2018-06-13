#import test


rootdir = "E:/Workplace/LIPDataset/Testing_images/"
path = "E:/Workplace/LIPDataset/Testing_images/testing_images/"
file = open(rootdir + 'test_id.txt', 'r')
"""
test_img = []
args.model_path = './ckpt/UperNet50.2-resnet50-upernet-ngpus2-batchSize12-imgMaxSize1000-paddingConst32-segmDownsampleRate4-LR_encoder0.02-LR_decoder0.02-epoch50-decay0.0001-fixBN0'
args.num_class = 20
args.suffix = '_epoch_2.pth'
args.arch_encoder = 'resnet50'
args.arch_decoder = 'upernet'
args.num_val = 10000
"""
for line in file:
    #rint(line)
    line = line.strip('\n')
    test_img = path + line + '.jpg'
    #test_img.append(path + line + '.jpg')
    print(test_img)
    #test.function(args)

"""
CUDA_VISIBLE_DEVICES=3
python3 test.py
--test_img /export/home/pjt/LIPData/Testing_images/testing_images/
--model_path ./ckpt/UperNet50.2-resnet50-upernet-ngpus2-batchSize12-imgMaxSize1000-paddingConst32-segmDownsampleRate4-LR_encoder0.02-LR_decoder0.02-epoch50-decay0.0001-fixBN0
--num_class 20
--suffix _epoch_2.pth
--arch_encoder 'resnet50'
--arch_decoder 'upernet'
--num_val 10000
"""
