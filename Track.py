#!/usr/bin/env python
import numpy as np
import cv2
import matplotlib.pyplot  as plt
import tkinter
import threading
import time


uh,us,uv,ub,ug,ur,ul,ua,ub_,lh,ls,lv,lb,lg,lr,ll,la,lb_=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
BGRSS_clicked,HSVSS_clicked,LABSS_clicked=0,0,0
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
crop_X1_tentative,crop_Y1_tentative,crop_X2_tentative,crop_Y2_tentative = -1,-1,-1,-1
crop_X1,crop_Y1,crop_X2,crop_Y2 = -1,-1,-1,-1
cropComplete = False

def roi(event,x,y,flags,param):

    global cropComplete,crop_X1_tentative,crop_Y1_tentative,crop_X2_tentative,crop_Y2_tentative

    if event == cv2.EVENT_LBUTTONDOWN:
     crop_X1_tentative = x
     crop_Y1_tentative = y
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
     crop_X2_tentative = crop_X1_tentative+200
     crop_Y2_tentative = crop_Y1_tentative+200
     cropComplete = True

cv2.namedWindow("image")
cv2.setMouseCallback("image", roi)

while True:

    ret, frame = cap.read()

    if cropComplete == True:
     cv2.rectangle(frame, (crop_X1_tentative,crop_Y1_tentative), (crop_X2_tentative,crop_Y2_tentative), (0, 255, 0), 2)

    cv2.imshow("image", frame)	  
	
    key = cv2.waitKey(1) & 0xFF
 
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
     cropComplete=False
	# if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
     crop_X1,crop_Y1,crop_X2,crop_Y2 = crop_X1_tentative,crop_Y1_tentative,crop_X2_tentative,crop_Y2_tentative
     cv2.destroyAllWindows() 
     break


 

    
def UH(H):
    global uh
    H=int(H)
    uh=H
    
def US(S):
    global us
    S=int(S)
    us=S
    
def UV(V):
    global uv
    V=int(V)
    uv=V
    
def UB(B):
    global ub
    B=int(B)
    ub=B
    
def UG(G):
    global ug
    G=int(G)
    ug=G
    
def UR(R):
    global ur
    R=int(R)
    ur=R
    
def UL(L):
    global ul
    L=int(L)
    ul=L
    
def UA(A):
    global ua
    A=int(A)
    ua=A
   
def UB___(B_):
    global ub_
    B_=int(B_)
    ub_=B_
    
def LH(H):
    global lh
    H=int(H)
    lh=H
    
def LS(S):
    global ls
    S=int(S)
    ls=S
   
def LV(V):
    global lv
    V=int(V)
    lv=V
    
def LB(B):
    global lb
    B=int(B)
    lb=B
    
def LG(G):
    global lg
    G=int(G)
    lg=G
    
def LR(R):
    global lr
    R=int(R)
    lr=R
  
def LL(L):
    global ll
    L=int(L)
    ll=L
    
def LA(A):
    global la
    A=int(A)
    la=A
    print(ll,la,lb_,"lrgb slider")
def LB___(B_):
    global lb_
    B_=int(B_)
    lb_=B_
def screenshotBGR():
 global BGRSS_clicked
 BGRSS_clicked=1 
 
def screenshotHSV():
 global HSVSS_clicked
 HSVSS_clicked=1
 
def screenshotLAB():
 global LABSS_clicked
 LABSS_clicked=1

class MyApp(tkinter.Frame):
 
  def __init__(self, master):
   global h,s,v,b,g,r,l,a,b,H,S,V,B,G,R,L,A,B_
   tkinter.Frame.__init__(self, master)
   master.title("Adjust Parameters")
   master.minsize(width=250, height=100)
   self.grid()
   BGRSS =tkinter.Button(text="BGR_Sshot", command=screenshotBGR)
   BGRSS.grid(row=0, column=0)
   HSVSS =tkinter.Button(text="HSV_Sshot", command=screenshotHSV)
   HSVSS.grid(row=0, column=1)
   LABSS =tkinter.Button(text="LAB_Sshot", command=screenshotLAB)
   LABSS.grid(row=0, column=2)
   UH_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='U H',command=UH)
   UH_.grid(row=1, column=0)
   LH_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='L H',command=LH)
   LH_.grid(row=1, column=1)
   US_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='U S',command=US)
   US_.grid(row=1, column=2)
   LS_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='L S',command=LS)
   LS_.grid(row=1, column=3)
   UV_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='U V',command=UV)
   UV_.grid(row=1, column=4)
   LV_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797061",label='L V',command=LV)
   LV_.grid(row=1, column=5)
   UB_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='U B',command=UB)
   UB_.grid(row=2, column=0)
   LB_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='L B',command=LB)
   LB_.grid(row=2, column=1)
   UG_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='U G',command=UG)
   UG_.grid(row=2, column=2)
   LG_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='L G',command=LG)
   LG_.grid(row=2, column=3)
   UR_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='U R',command=UR)
   UR_.grid(row=2, column=4)
   LR_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#8da792",label='L R',command=LR)
   LR_.grid(row=2, column=5)
   UL_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='U L',command=UL)
   UL_.grid(row=3, column=0)
   LL_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='L L',command=LL)
   LL_.grid(row=3, column=1)
   UA_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='U A',command=UA)
   UA_.grid(row=3, column=2)
   LA_=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='L A',command=LA)
   LA_.grid(row=3, column=3)
   UB__=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='U B',command=UB___)
   UB__.grid(row=3, column=4)
   LB__=tkinter.Scale(from_=0,to=255,orient="vertical",bg="#797979",label='L B',command=LB___)
   LB__.grid(row=3, column=5)
   
 
def slider():
 root = tkinter.Tk()
 
 app = MyApp(root)
 app.mainloop()	
 
p1 = threading.Thread(target=slider)


p1.start()

#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)


#hsv_for_hist = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#Roi_hist=cv2.calcHist([frame],[2],maskedImage,[256],[0,256])
#cv2.normalize(Roi_hist,Roi_hist,0,255,cv2.NORM_MINMAX)

while True:
  #print(lr,lg,lb,"while")
  ret, frame = cap.read()
  gray_= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray=gray_
  #cv2.imshow("gray_scale",gray)
  gray_shape=gray.shape    	
  mask_ =np.ones(gray_shape,np.uint8)
  mask_=mask_*255
  mask_[crop_Y1:crop_Y2 , crop_X1:crop_X2]=0
  mask_inv=cv2.bitwise_not(mask_) #mask inv for colour?(yes)
  #ROI
  cv2.rectangle(frame, (crop_X1_tentative,crop_Y1_tentative), (crop_X2_tentative,crop_Y2_tentative), (0, 255, 0), 2)
  cv2.imshow("ROI", frame)
  #RGB 
  maskedImage_RGB = cv2.bitwise_and( frame , frame ,mask = mask_inv)
  lower_rgb = np.array([lr,lg,lb])
  upper_rgb = np.array([ur,ug,ub])
  #print(lr,lg,lb,"lr,lg,lb")
  maskedImage_RGB_= cv2.inRange(maskedImage_RGB, lower_rgb, upper_rgb)
  maskedImage_RGB_crop=maskedImage_RGB_[crop_Y1:crop_Y2 , crop_X1:crop_X2]
  cv2.imshow("RGB", maskedImage_RGB_crop)
  #HSV
  hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  maskedImage_hsv= cv2.bitwise_and( hsv , hsv ,mask = mask_inv)
  lower_hsv = np.array([lh,ls,lv])
  upper_hsv = np.array([uh,us,uv])
  maskedImage_hsv_= cv2.inRange(maskedImage_hsv, lower_hsv, upper_hsv)
  maskedImage_hsv_crop=maskedImage_hsv_[crop_Y1:crop_Y2 , crop_X1:crop_X2]
  cv2.imshow("hsv", maskedImage_hsv_crop)
  #LAB
  lab= cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
  maskedImage_lab = cv2.bitwise_and( lab , lab ,mask = mask_inv)
  lower_lab = np.array([ll,la,lb_])
  upper_lab = np.array([ul,ua,ub_])
  
  maskedImage_lab_= cv2.inRange(maskedImage_lab , lower_lab, upper_lab)
  maskedImage_lab_crop=maskedImage_lab_[crop_Y1:crop_Y2 , crop_X1:crop_X2]
  cv2.imshow("lab", maskedImage_lab_crop)
  #maskedImage = maskedImage[:,:]
  
  #print(BGRSS_clicked,"bgrs_clicked")
  ##write images
  if BGRSS_clicked == 1:
   a=maskedImage_RGB_crop
   cv2.imwrite("Noise.png",a)
   BGRSS_clicked =0
  elif HSVSS_clicked==1:
   a=maskedImage_hsv_crop
   cv2.imwrite("Noise.png",a)
   HSVSS_clicked=0
  elif LABSS_clicked== 1:
   a=maskedImage_lab_crop
   cv2.imwrite("Noise.png",a)
   LABSS_clicked= 0
  key = cv2.waitKey(1) & 0xFF	
  if key== ord('q'):
   cv2.destroyAllWindows()
   break   
  




		
    
cap.release()
cv2.destroyAllWindows() 
	 
