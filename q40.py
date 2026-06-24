import cv2

# Load image
img = cv2.imread(
    r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp"
)

# Rectangle coordinates
x, y, w, h = 100, 100, 200, 200

# Draw rectangle
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    2
)

# Extract object (crop)
object_img = img[y:y+h, x:x+w]

# Display images
cv2.imshow("Image with Rectangle", img)
cv2.imshow("Extracted Object", object_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
