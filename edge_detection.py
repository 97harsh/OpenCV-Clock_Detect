import cv2
import numpy as np

# file1=r"./flower1.jpg"
# img1=cv2.imread(file1,)

# laplacian =cv2.Laplacian(img1,cv2.CV_64F)

# cv2.imshow('image',img1)
# cv2.imshow('laplacian',laplacian,)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap=cv2.VideoCapture(0) #capture 0 i.e. first webcam


while True:
    _,frame=cap.read()
    laplacian =cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,200,200,)

    cv2.imshow('laplacian',laplacian)
    # cv2.imshow('sobelx',sobelx)
    # cv2.imshow('sobely',sobely)
    cv2.imshow('frame',frame)
    cv2.imshow('canny',edges)

    if(cv2.waitKey(1) & 0xFF== ord('q') ): # q to quit
        break

cap.release() ## to realease the camera
cv2.destroyAllWindows()

