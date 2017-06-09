import numpy as np
import cv2
import matplotlib.pyplot as plt
class tools:

    def display(self,a):
        cv2.imshow('image',a)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def draw(self,img):
        cv2.line(img,(0,0),(1150,1150),(0,0,255),1)
        cv2.rectangle(img,(150,150),(40,400),(0,255,0),1)
        cv2.circle(img,(275,275),125,(255,0,0),1)
        pts = np.array([[100,200],[200,300],[350,350],[300,200],[200,100]],np.int32)
        cv2.polylines(img,[pts],True,(0,255,0),1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'test',(150,150),font,2,(200,200,00),2,cv2.LINE_AA)
img = cv2.imread('imgtestme.jpg',1)

