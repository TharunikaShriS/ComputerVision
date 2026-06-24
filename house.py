import cv2
import numpy as np

# Create a white image
img = np.ones((600, 600, 3), dtype=np.uint8) * 255

# House body
cv2.rectangle(img, (180, 220), (420, 450), (0, 0, 255), 3)

# Roof
roof_points = np.array([[180, 220], [300, 100], [420, 220]], np.int32)
cv2.polylines(img, [roof_points], True, (0, 255, 0), 3)

# Door
cv2.rectangle(img, (270, 330), (330, 450), (255, 0, 0), 3)

# Left window
cv2.rectangle(img, (210, 260), (260, 310), (255, 0, 255), 3)

# Right window
cv2.rectangle(img, (340, 260), (390, 310), (255, 0, 255), 3)

# Window lines
cv2.line(img, (235, 260), (235, 310), (255, 0, 255), 2)
cv2.line(img, (210, 285), (260, 285), (255, 0, 255), 2)

cv2.line(img, (365, 260), (365, 310), (255, 0, 255), 2)
cv2.line(img, (340, 285), (390, 285), (255, 0, 255), 2)

# Door knob
cv2.circle(img, (320, 390), 4, (0, 0, 0), -1)

# Chimney
cv2.rectangle(img, (340, 130), (370, 200), (0, 165, 255), 3)

# Sun
cv2.circle(img, (500, 100), 40, (0, 255, 255), 3)

# Ground
cv2.line(img, (0, 450), (600, 450), (0, 128, 0), 3)

# Display
cv2.imshow("House Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
