import json
import random
import numpy as np
from PIL import Image

def cut_generator(idx):

    image_name = "/home/ubuntu/TextFuseNet/datasets/icdar2013/train_images/ICDAR2013_Train_"
    image1 = image_name + str(idx+100) + ".jpg"
    img1 = Image.open(image1).resize((300, 300))
    img1.save("/home/ubuntu/TextFuseNet/datasets/resized_icdar2013/train_images/ICDAR2013_Train_"  + str(idx+100) + ".jpg")

for i in range(229):
    cut_generator(i)