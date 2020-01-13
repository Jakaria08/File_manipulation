import os
import glob
import cv2

image_path = "/home/jakaria/Super_Resolution/CinCGAN-pytorch/datasets/SPOT-6-BING/DIV2K/DIV2K_train_HR"
count = 1

for img_file in glob.glob(image_path + '/*.png'):
    dir_name = os.path.join(os.dirname(image_path), "DIV2K_train_LR_bicubic")

    img =  cv2.imread(img_file)
    resize_image = cv2.resize(img, (256,256), interpolation=cv2.INTER_CUBIC)

    new_name = os.path.join(dir_name, str(count).zfill(4) + "x4.png")
    cv.imwrite(new_name, resize_image)

    count += 1
    if count%100 == 0:
        print(count)
