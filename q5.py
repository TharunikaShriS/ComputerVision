import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/ACER/Downloads/9303b11bd1e69409db70136a97891604.webp")

# Get image dimensions
rows, cols = img.shape[:2]

# Translation values
tx = 100   # Shift right by 100 pixels
ty = 50    # Shift down by 50 pixels

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
translated = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()
