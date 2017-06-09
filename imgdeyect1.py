import cv2
import numpy as np 
import opencv1 as cv1 

img=cv2.imread('imgtestme.jpg')
edge= cv2.Canny(img,130,150)
cv2.imshow('image',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cap = cv2.VideoCapture(0)
#while True:
    #
    # _, frame=cap.read()
    #laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    #sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    #edges= cv2.Canny(frame,150,100)
    #cv2.imshow('orignal',laplacian)
    #cv2.imshow('orignal',sobelx)
    #cv2.imshow('orignal',sobely)
    #cv2.imshow('orignal',edges)
    #k=cv2.waitKey(5) & 0xFF
    #if k ==27:
     #   break

    
#cv2.destroyAllWindows()
#cap.release()        