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

five_path="C:/Users/John/Milestone/image_edit/image_shots/5"
print("five")

five_name=list()
print(type(five_name))
five_images=pd.DataFrame()
for x in os.listdir(five_path):
 print (x)
 #print(type(five_name))
 five_name.append(5)
 withpath=five_path+"/"+x
 a=cv2.imread(withpath)
 singlea=a[:,:,0]
 raveled=singlea.ravel()
 raveled_=pd.Series(raveled)
 five_images=five_images.append(raveled_,ignore_index=True)
#print(images.head)

L_path="C:/Users/John/Milestone/image_edit/image_shots/L"
print("L")
L_name=list()
L_images=pd.DataFrame()
for x in os.listdir(L_path):
 print (x)
 L_name.append(2)
 withpath=L_path+"/"+x
 a=cv2.imread(withpath)
 singlea=a[:,:,0]
 raveled=singlea.ravel()
 raveled_=pd.Series(raveled)
 L_images=L_images.append(raveled_,ignore_index=True)
print(L_images.head)

Noise_path="C:/Users/John/Milestone/image_edit/image_shots/Noise"
print("Noise")
Noise_name=list()
Noise_images=pd.DataFrame()
for x in os.listdir(Noise_path):
 print (x)
 Noise_name.append(0)
 withpath=Noise_path+"/"+x
 a=cv2.imread(withpath)
 singlea=a[:,:,0]
 raveled=singlea.ravel()
 raveled_=pd.Series(raveled)
 Noise_images=Noise_images.append(raveled_,ignore_index=True)

#print(images.head)
mixed_names=list()

mixer=pd.DataFrame()
shape=Noise_images.shape
counter=list(range(0,shape[0]))
for x in counter:
 #print(x,y,z)
 #print(type(Noise_images),type(L_images),type(five_images))
 mixer=mixer.append(Noise_images.iloc[x])
 mixer=mixer.append(L_images.iloc[x])
 mixer=mixer.append(five_images.iloc[x])
 
for a in zip(Noise_name,L_name,five_name):
 print(a[0])
 print(a[1])
 print(a[2])
 mixed_names.append(a[0])
 mixed_names.append(a[1])
 mixed_names.append(a[2])
 
print(mixer.head)
#print(mixed_names[0])
handle=open("mixed_images.pickle","wb")
pickle.dump(mixer,handle,protocol=pickle.HIGHEST_PROTOCOL)
handle.close()

handle_=open("mixed_names.pickle","wb")
pickle.dump(mixed_names,handle_,protocol=pickle.HIGHEST_PROTOCOL)
handle.close()


