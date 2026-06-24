import cv2

# Read the image
img = cv2.imread("C:/Users/ACER/Downloads/9303b11bd1e69409db70136a97891604.webp")

# Rotate 90 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display the original and rotated images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
