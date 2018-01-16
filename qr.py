
import cv2
import numpy as np

img=cv2.imread("qr.jpg",1)

img=cv2.resize(img,(480,640))
im=img
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh,i=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
i=cv2.bitwise_not(i)
i=cv2.dilate(i,None,iterations=7)
i=cv2.erode(i,None,iterations=3)
image,contours,heirarchy=cv2.findContours(i,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


if(contours):
    
    area=[cv2.contourArea(cnt) for cnt in contours]
    index=np.argmax(area)
    cnt=contours[index]
    x,y,w,h=cv2.boundingRect(cnt)
    cv2.imwrite("barcode.jpg",im[y:y+h,x:x+w])
    cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('fame',im)
    
    cv2.waitKey(0)
