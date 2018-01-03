#!/usr/bin/env python
import numpy as np
import cv2
import matplotlib.pyplot  as plt
import tkinter
import threading
import time
from PIL import Image, ImageTk

global screen,imagelist,thumblist,choice,lmain

imagelist=[]
thumblist=[]

cap = cv2.VideoCapture(0)

def camera():
 global screen
 while True:
  ret, frame = cap.read()
  screen=frame
  cv2.imshow("image", screen)	  	
  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
    break


	
def Record():
    global screen,root,thumblist,lmain
    cv2image = cv2.cvtColor(screen, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    size=100,100
    #thumb=img.thumbnail(size)
    imagelist.append(img)
    img.thumbnail(size)
    thumblist.append(img)
              
    lmain=None
    #print(thumblist)
    for image in thumblist:
     print(image)
     imgtk = ImageTk.PhotoImage(image=image)
     if lmain==None:
      lmain = tkinter.Label(root,image=imgtk)
      lmain.image = imgtk
      lmain.pack()
     else:
      lmain.destroy()
      lmain = tkinter.Label(root,image=imgtk)
      #lmain=tkinter.Button(image=imgtk)
      lmain.image = imgtk
      lmain.pack()
      
	 
class MyApp(tkinter.Frame):
  
  def __init__(self, master):
   global thumblist,a
   tkinter.Frame.__init__(self, master)
   master.title("select Images")
   master.minsize(width=250, height=100)
   self.pack()
   record =tkinter.Button(text="Record", command=Record)
   record.pack()
   self.choice=tkinter.Entry(text="Type Item to delete")
   #choice_value=choice.get()
   self.choice.pack()
   Delete=tkinter.Button(text="Delete", command=self.delete_img)
   Delete.pack()
  def delete_img(self):
    global lmain
    a=self.choice.get()
    b=int(a)
    thumblist.pop(b)
    tkinter.update()
    
	
	
p1 = threading.Thread(target=camera)
p1.start()  

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()	
 



