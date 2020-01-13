import os
import glob

image_path = "/home/jakaria/Super_Resolution/CinCGAN-pytorch/datasets/SPOT-6-BING/DIV2K/DIV2K_valid_LR_mild"
count = 801

for img_file in glob.glob(image_path + '/*.png'):
    dir_name = os.path.dirname(img_file)
    new_name = os.path.join(dir_name, str(count).zfill(4) + ".png")
    os.rename(img_file,new_name)
    count += 1
    if count%100 == 0:
        print(count)
