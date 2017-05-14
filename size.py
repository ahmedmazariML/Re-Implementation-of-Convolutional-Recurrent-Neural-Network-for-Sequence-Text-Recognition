from __future__ import division
import cv2
import numpy as np
import csv
import os
import pandas as pd
import glob
from matplotlib import pyplot as plt


path="/home/ahmed/Downloads/training_data/train/"
path_output="/home/ahmed/Downloads/training_data/train_scaled"
os.chdir(path)
WIDTH=[]
HEIGHT=[]

images_name = glob.glob("*.jpg")

for img in images_name:
    image=cv2.imread(path+img)
    os.chdir(path_output)
    image=cv2.resize(image, (100, 32), interpolation=cv2.INTER_NEAREST)

    cv2.imwrite(img,image)
    h,w=image.shape[0:2]
    HEIGHT.append(h)
    WIDTH.append(w)
print("height",HEIGHT)
print("width",WIDTH)

'''
for img in images_name:
    w, h = img.shape[0:2]
    WIDTH.append(w)
    HEIGHT.append(h)
max_width = max(WIDTH)
max_height = max(HEIGHT)

'''
