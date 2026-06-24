import cv2
import numpy as np
img=cv2.imread("C:/Users/ACER/Downloads/9303b11bd1e69409db70136a97891604.webp")
angle=45
scale=1.0
rotation=cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2),angle,scale)
output=cv2.warpAffine(img,rotation,(img.shape[1],img.shape[0]))
cv2.imshow("original",img)
cv2.imshow("transformed",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
