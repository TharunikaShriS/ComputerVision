import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Source points (replace with your image coordinates)
src = np.float32([[100,100], [400,100], [450,400], [80,400]])

# Destination points
dst = np.float32([[0,0], [300,0], [300,400], [0,400]])

# Perspective transform
M = cv2.getPerspectiveTransform(src, dst)
output = cv2.warpPerspective(img, M, (300,400))

cv2.imshow("Original", img)
cv2.imshow("Transformed", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
