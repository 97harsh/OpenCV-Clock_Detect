import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0) #capture 0 i.e. first webcam
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))
#to write the output 
## not working will work more on that


while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # will have gray colored frame of webcam image
    
    out.write(frame)
    cv2.imshow('frame',frame) #color frame
    cv2.imshow('gray',gray) # gray frame

    if(cv2.waitKey(1) & 0xFF== ord('q') ): # q to quit
        break

cap.release() ## to realease the camera
out.release() ## to release the recording saver
cv2.destroyAllWindows()


