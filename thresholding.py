import cv2
import numpy as np
import matplotlib.pyplot as plt

file=r"./book.jpg"
img=cv2.imread(file,)
cv2.imshow('image',img) #image

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, threshold=cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) # as low light image
retval2, threshold2=cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold) # the thresholded image
cv2.imshow('gray',grayscaled)
cv2.imshow('thresholdgray',threshold2)
#adaptive gaussian threshold
gauss=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('gauss',gauss)
retval2, otsu=cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu',otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()