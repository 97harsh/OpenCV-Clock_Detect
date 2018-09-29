import cv2
import numpy as np

file1=r"./flower1.jpg"
img1=cv2.imread(file1,)

hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)



lower_green=np.array([40,0,0]) 
#to be set to detect color whatever you want to be detected
upper_green=np.array([80,255,255])
kernel=np.ones((15,15),np.float32)/(15*15)

# cv2.imshow("frame",frame,)
mask=cv2.inRange(hsv,lower_green,upper_green) 
# cv2.imshow('mask',mask)
#currently mask is only green
res=cv2.bitwise_and(img1,img1,mask=mask)
cv2.imshow("res",res)
kernel=np.ones((5,5),np.uint8)
erosion =cv2.erode(mask,kernel,iterations=1)
res1=cv2.bitwise_and(img1,img1,mask=erosion)
dilation =cv2.dilate(mask,kernel,iterations=1)
res2=cv2.bitwise_and(img1,img1,mask=dilation)

opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
#opening removes false positives
reso=cv2.bitwise_and(img1,img1,mask=opening)
closing= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
#closing removes false negatives
resc=cv2.bitwise_and(img1,img1,mask=closing)

cv2.imshow('erosion',res1)
cv2.imshow('dilation',res2)
cv2.imshow('opening',reso)
cv2.imshow('closing',resc)


cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
