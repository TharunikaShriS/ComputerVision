import cv2
import numpy as np

# Load image
img = cv2.imread(
    r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp",
    cv2.IMREAD_GRAYSCALE
)

# Convert to binary image
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply Closing
closing = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel
)

# Display images
cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Result", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
