import numpy as np 
import cv2
import opencv1 as cv1
img=cv2.imread('imgtestme.jpg',cv2.IMREAD_COLOR)
#img[555,555]=[255,255,255]
#px=img[555,555]
#print(px)
img[200:300,200:300]=img[600:700,600:700]
print(img[600:700,600:700])
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
