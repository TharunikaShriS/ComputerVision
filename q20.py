import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Laplacian sharpening mask (negative center coefficient)
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

# Apply mask
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
