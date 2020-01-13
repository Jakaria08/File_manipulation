import os
import glob

image_path = "/home/jakaria/Super_Resolution/CinCGAN-pytorch/datasets/SPOT-6-BING/DIV2K/DIV2K_train_HR"
count = 1

for img_file in glob.glob(image_path + '/*.png'):
    new_name = str(count).zfill(4) + ".png"
    print(new_name)
    count += 1
    if count%100 == 0:
        print(count)
