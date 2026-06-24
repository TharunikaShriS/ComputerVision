import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Source and destination points
src = np.float32([[100,100], [500,100], [550,400], [50,400]])
dst = np.float32([[0,0], [400,0], [400,500], [0,500]])

# Compute Homography Matrix
H, _ = cv2.findHomography(src, dst)

# Apply perspective transformation
warped = cv2.warpPerspective(img, H, (400, 500))

cv2.imshow("Original", img)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
