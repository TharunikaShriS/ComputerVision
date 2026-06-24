import cv2

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel edge detection (X and Y axes)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y gradients
sobel_xy = cv2.magnitude(sobel_x, sobel_y)
sobel_xy = cv2.convertScaleAbs(sobel_xy)

cv2.imshow("Original", img)
cv2.imshow("Sobel X+Y", sobel_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
