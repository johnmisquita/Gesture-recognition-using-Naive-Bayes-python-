#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot  as plt
import pandas as pd
import imageio
from sklearn.svm import SVC
from skimage import io
import os,os.path
import cv2
import pickle 

noise_path="C:/Users/John/Milestone/image_edit/image_shots/Noise"
rotated=[]
counter=0
for x in os.listdir(noise_path):
 counter=counter+1
 print (x)
 #print(type(five_name))
 withpath=noise_path+"/"+x
 img=cv2.imread(withpath)
 cols = img.shape
 matrix = cv2.getRotationMatrix2D((cols[1]/2,cols[0]/2),90,1)
 rotated= cv2.warpAffine(img,matrix,(cols[1],cols[0]))
 cv2.imwrite("%s.png"%(counter),rotated)
#print(images.head)