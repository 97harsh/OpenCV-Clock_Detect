import cv2
import numpy as np

file1=file1=r"./flower1.jpg"
img1=cv2.imread(file1,)

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #convert to hsv value from BGR
    #hsv =hue, sat, value
    
    lower_green=np.array([40,0,0]) 
    #to be set to detect color whatever you want to be detected
    upper_green=np.array([80,255,255])
    kernel=np.ones((15,15),np.float32)/(15*15)

    # cv2.imshow("frame",frame,)
    mask=cv2.inRange(hsv,lower_green,upper_green) 
    # cv2.imshow('mask',mask)
    #currently mask is everything
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("res",res)
    # smoothed=cv2.filter2D(res,-1,kernel)
    # # cv2.imshow('smoothed',smoothed)
    # blur=cv2.GaussianBlur(res,(15,15),0)
    # median=cv2.medianBlur(res,15)
    # # cv2.imshow('median',median)
    # bilateral=cv2.bilateralFilter(res,15,75,75)
    # cv2.imshow('bilateral',bilateral)
    # cv2.imshow('blur',blur)


    if(cv2.waitKey(1) & 0xFF== ord('q') ): # q to quit
        break

cv2.destroyAllWindows()
cap.release()

