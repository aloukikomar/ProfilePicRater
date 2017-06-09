import cv2
import numpy as np 
import opencv1 as cv1 
img=cv2.imread('imgtestme.jpg')
retval, threshold = cv2.threshold(img,100,150,cv2.THRESH_BINARY)
print(threshold)
cv2.imshow('image',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
