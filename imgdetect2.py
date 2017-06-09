import cv2
import numpy as np 
import opencv1 as cv1 

imgc=cv2.imread('chess1.png',1)
temp=cv2.imread('chess2.png',0)
w,h=temp.shape[::-1]

imgca= cv2.Canny(imgc,100,100)
temp= cv2.Canny(temp,100,100)
res=cv2.matchTemplate(imgca,temp,cv2.TM_CCOEFF_NORMED)
threshold=0.75
loc=np.where(res>=threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(imgc,pt,(pt[0]+w,pt[1]+h),(255,255,255),1)
cv2.imshow('image',imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
