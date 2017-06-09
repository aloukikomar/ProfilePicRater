import cv2
import numpy as np 
import opencv1 as cv1 
img=cv2.imread('imgtestme2.jpg')

imgrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faceC=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeC=cv2.CascadeClassifier('haarcascade_eye.xml')
smileC=cv2.CascadeClassifier('haarcascade_smile.xml')
faces=faceC.detectMultiScale(imgrey,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    faceD=img[y:y+w,x:x+h]
    eyes=eyeC.detectMultiScale(imgrey,1.3,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)
    smile=smileC.detectMultiScale(imgrey,1.3,5)
    for (sx,sy,sw,sh) in eyes:
        cv2.rectangle(img,(sx,sy),(sx+sw,sy+sh),(0,0,255),1)

h,w=img.shape[:2]
img = cv2.resize(img, (1000, 1000),interpolation=cv2.INTER_AREA) 
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000 ,1000)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
