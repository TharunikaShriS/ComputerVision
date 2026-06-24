import cv2

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel edge detection (Y-axis)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to 8-bit
sobel_y = cv2.convertScaleAbs(sobel_y)

cv2.imshow("Original", img)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
