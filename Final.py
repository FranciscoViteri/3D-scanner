# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:05:48 2021

@author:
Francisco
Javier
jonat
"""

# import the necessary packages
import cv2
import numpy as np
import pyautocad
from pyautocad import APoint
import matplotlib.pyplot as plt
acad=pyautocad.Autocad()
#print(cv2.__version__)
image = cv2.imread('Cortado.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
lower= np.array([60,60,60])
higher =np.array([254,254,254])
mask = cv2.inRange(image, lower, higher)
mask.shape
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#canny = cv2.Canny(gray, 10, 150)
canny = cv2.Canny(gray, 10,150)

canny = cv2.dilate(canny, None, iterations=1)

canny = cv2.erode(canny, None, iterations=1)
cv2.imshow('canny',canny)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# OpenCV 4
#cv2.drawContours(image, cnts, -1, (255,0,0), 2)
cont_img = cv2.drawContours(image, cnts, -1, 254, 3)
Ancho=107.188
PAncho=720
Alto=67.6275
PAlto=554
contador=0

for c in cnts:
    #epsilon = 0.01*cv2.arcLength(c,True)
    epsilon = 0.001*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)

    print([approx])
    #p1=APoint(45,20)
    print(len(approx))
    cv2.drawContours(image, [approx], 0, (0,255,0),2)
    print(approx[0][0][0])
    contador=0
    while True:
        
        pi=APoint((approx[contador][0][0]*Ancho/PAncho),((approx[contador][0][1]*(-1)+PAlto)*Alto/PAlto))
        contador = contador + 1
        pf=APoint((approx[contador][0][0]*Ancho/PAncho),((approx[contador][0][1]*(-1)+PAlto)*Alto/PAlto))
        linea=acad.model.AddLine(pi,pf)
        if contador == (len(approx)-1):
            pin=APoint((approx[0][0][0]*Ancho/PAncho),((approx[0][0][1]*(-1)+PAlto)*Alto/PAlto))
            linea=acad.model.AddLine(pin,pf)
            break
        
cv2.imshow('image',image)
    #cv2.imshow('image',imageOut)
cv2.waitKey(0)
plt.figure(figsize=(20,20))
plt.subplot(1, 2, 1), plt.imshow(mask)
plt.subplot(1, 2, 2), plt.imshow(cont_img)
plt.show()
