import cv2
import numpy as np
import matplotlib.pyplot as plt

file=r"./download.jpeg"
img=cv2.imread(file,cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR ## other different formats
#IMREAD_UNCHANGED

# plt.imshow(img,cmap="gray",interpolation='bicubic')
# plt.plot([50,100],[80,100],'c',linewidth=5) #line drawn on image 
# plt.show()

cv2.imshow("IMAGE",img)
cv2.waitKey(0) ## opencv does BGR and matplotlib does RGB so 
cv2.destroyAllWindows() ##quits when a key is pressed

# cv2.imwrite("<name>",<array>) #used to save image

