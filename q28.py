import cv2
import numpy as np

# Load image
img = cv2.imread(
    r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp",
    cv2.IMREAD_GRAYSCALE
)

# Check if image loaded
if img is None:
    print("Image not found!")
    exit()

# Sharpening kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply convolution with reflected boundary handling
result = cv2.filter2D(
    img,
    ddepth=-1,
    kernel=kernel,
    borderType=cv2.BORDER_REFLECT
)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Sharpened", result)

# Save output
cv2.imwrite(
    r"C:\Users\ACER\Downloads\sharpened_output.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()
