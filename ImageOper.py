import cv2
import matplotlib.pyplot as plt
import numpy as np

file=r"./download1.jpeg"
img=cv2.imread(file,cv2.IMREAD_COLOR)
#image analysis easier to do on gray image so done on 
#gray image find
#objects and mark on color image

img[55,55]=[255,255,255]

px=img[55,55] 

# img[100:150,100:150]=[255,255,255]
# roi=img[100:150,100:150]  #converting parts of images

# print(px)

face=img[100:150,100:150]

#Region of Image  
img[0:50,0:50]=face
img[100:150,100:150]=[255,255,255] #cut pasting the image


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(roi)
