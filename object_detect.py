import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
# clock_detect=cv2.CascadeClassifier('clock_8_cascade.xml')

cap=cv2.VideoCapture(0)

while True:
    ret, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    # clock=cv2.CascadeClassifier.detectMultiScale(gray,clock_detect,scale_factor=.5,min_size=(10,10),max_size=(40,40))
    # clock=clock_detect.detectMultiScale(gray,2,10)
    # for (x,y,w,h) in clock:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2,cv2.LINE_AA)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),((x+w),y+h),(255,0,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'face',(x+w,y+h), font, 2,(255,255,255),2,cv2.LINE_AA)
        # #faces will be inside the face so usefult to detect inside face
        # roi_gray=gray[y:y+h,x:x+w]
        # roi_color=img[y:y+h,x:x+w]
        # # eyes=eye_cascade.detectMultiScale(roi_gray)
        # # for (ex,ey,eh,ew) in eyes:
        # #     cv2.rectangle(roi_color,(ex,ey),((ex+ew),ey+eh),(0,255,0),2)
        # cv2.putText(roi_color,'eye',(ex+ew,ey+eh), font, 1,(255,255,255),2,cv2.LINE_AA)
        # cv2.imshow('img',img)
    if(0xFF== ord('q') ): # q to quit
        break

cap.release() ## to realease the camera
cv2.destroyAllWindows()


