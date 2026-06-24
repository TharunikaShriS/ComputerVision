import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Source and destination points
src = np.array([[100,100], [500,100], [550,400], [50,400]], dtype=float)
dst = np.array([[0,0], [400,0], [400,500], [0,500]], dtype=float)

# DLT
A = []
for (x,y), (u,v) in zip(src, dst):
    A.append([-x,-y,-1,0,0,0,u*x,u*y,u])
    A.append([0,0,0,-x,-y,-1,v*x,v*y,v])

A = np.array(A)
_, _, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3,3)

# Perspective transformation
warped = cv2.warpPerspective(img, H, (400,500))

cv2.imshow("Original", img)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
