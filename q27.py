import cv2

img = cv2.imread(r"C:\Users\ACER\Downloads\9303b11bd1e69409db70136a97891604.webp")

# Crop center region
crop = img[100:300, 100:300]

# Paste at another location in same image
img[350:550, 350:550] = crop

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
