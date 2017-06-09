import cv2
import numpy as np 
import opencv1 as cv1 
import matplotlib.pyplot as plt
img=cv2.imread('imgtestme.jpg')
#edge= cv2.Canny(img,130,150)
mask=np.zeros(img.shape[:2],np.uint8)
bg= np.zeros((1,65),np.float64)
fg= np.zeros((1,65),np.float64)
rect=(50,50,800,400)
cv2.grabCut(img,mask,rect,bg,fg,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
