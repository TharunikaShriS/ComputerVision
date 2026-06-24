import cv2

# Read image
img = cv2.imread("C:/Users/ACER/Downloads/Spiderman.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Outline using Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
