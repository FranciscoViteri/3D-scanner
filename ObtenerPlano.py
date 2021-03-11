# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:10:11 2021

@author:
Francisco
Javier
jonat
"""

import cv2
import numpy as np

def clics(event,x,y,flags,param):
	global puntos
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(imagen,(x,y),5,(0,255,0),2)
		puntos.append([x,y])

def uniendo4puntos(puntos):
	cv2.line(imagen,tuple(puntos[0]),tuple(puntos[1]),(255,0,0),1)
	cv2.line(imagen,tuple(puntos[0]),tuple(puntos[2]),(255,0,0),1)
	cv2.line(imagen,tuple(puntos[2]),tuple(puntos[3]),(255,0,0),1)
	cv2.line(imagen,tuple(puntos[1]),tuple(puntos[3]),(255,0,0),1)

puntos = []
#lectura imagen
imagen = cv2.imread('im4.jpg')
aux = imagen.copy()
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen',clics)

while True:

	if len(puntos) == 4:
		uniendo4puntos(puntos)
		pts1 = np.float32([puntos])
		pts2 = np.float32([[0,0], [720,0], [0,554], [720,554]])

		M = cv2.getPerspectiveTransform(pts1,pts2)
		dst = cv2.warpPerspective(imagen, M, (720,554))

		cv2.imshow('dst', dst)
        
	cv2.imshow('Imagen',imagen)
	
	k = cv2.waitKey(1) & 0xFF
	if k == ord('n'):
		imagen = aux.copy()
		puntos = []
		cv2.imwrite('Cortado.png',dst)
	elif k == 27:
		break

cv2.destroyAllWindows()
