import cv2
import numpy as np

# Load image
img = cv2.imread(
    r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp",
    cv2.IMREAD_GRAYSCALE
)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Morphological Gradient
gradient = cv2.morphologyEx(
    img,
    cv2.MORPH_GRADIENT,
    kernel
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Morphological Gradient", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
