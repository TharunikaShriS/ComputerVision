import cv2

# Read image
img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display result
cv2.imshow("Original", img)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
