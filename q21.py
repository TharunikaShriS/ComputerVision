import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Check if image loaded successfully
if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to float for processing
img_float = img.astype(np.float32)

# Laplacian mask with diagonal extension (8-neighbor)
laplacian_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply sharpening
sharpened = cv2.filter2D(img_float, -1, laplacian_kernel)

# Clip values to valid range
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

# Save result
cv2.imwrite("sharpened_output.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
