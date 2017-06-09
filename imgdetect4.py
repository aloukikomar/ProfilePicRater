import cv2
import numpy as np 
import opencv1 as cv1 
img=cv2.imread('imgtestme.jpg')
imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgrey= np.float32(imgrey)

corners= cv2.goodFeaturesToTrack(imgrey,500,0.009,20)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()