import cv2
import numpy as np
import matplotlib.pyplot as plt

file1=r"./flower1.jpg"
file2=r"./flower2.jpg"
file3=r"./python.png"

img1=cv2.imread(file2,)
img2=cv2.imread(file3,)

rows,cols,channels=img2.shape
roi=img1[0:rows][0:cols]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,210,255,cv2.THRESH_BINARY_INV) #
#masked value #threshold helps simplify images by 
# removing high values from background maybe
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows][0:cols]=dst

cv2.imshow('rest',dst)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('mask',mask)

# add=img1+img2 #simple addition on opaqueness in images
# add=cv2.add(img1,img2) # added upto max 255 #using inbuilt function
# cv2.imshow('1',img1)
# cv2.imshow('2',img2)
# weighted=cv2.addWeighted(img1,.6,img2,.4,0) #weigthed sum

# cv2.imshow('add',add)
# cv2.imshow('weight',weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()

