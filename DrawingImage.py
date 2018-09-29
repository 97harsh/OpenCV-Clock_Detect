import cv2
import matplotlib.pyplot as plt
import numpy as np

file=r"./flower2.jpg"
img=cv2.imread(file,cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_green=np.array([40,0,0]) ## lower_green - higher_green
# only green left in image after using this to mask
#to be set to detect color whatever you want to be detected
upper_green=np.array([80,255,255])
mask=cv2.inRange(hsv,lower_green,upper_green)
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("res",res)
#line
# cv2.line(img,(0,0),(150,150),(255,255,255),15, ) #bgr format in opencv

#rectangle
# cv2.rectangle(img,(10,10),(150,150),(0,255,255),5)  #bgr format

#circle
# cv2.circle(img,(50,50),20,(100,255,35),-1) 
# -1 to fill circles

#polygon
# pts=np.array([[10,20],[25,35],[65,36],[65,69],[95,36]],np.int32)
# pts=pts.reshape((-1,1,2)) # to reshape 

# cv2.polylines(img,[pts],True,(255,0,0),5,)

#writing text
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,"Open CV writing",(0,100),font,5,(0,255,36),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

