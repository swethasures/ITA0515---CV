import cv2
import numpy as np


image = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306300126.jpg")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


low_pass = cv2.GaussianBlur(gray, (5, 5), 0)

boost_factor = 2.0

high_boost = gray + boost_factor * (gray - low_pass)

high_boost = np.clip(high_boost, 0, 255)

high_boost_color = cv2.cvtColor(high_boost.astype(np.uint8), cv2.COLOR_GRAY2BGR)

cv2.imshow("Original Image", image)
cv2.imshow("High-Boost Filtered Image", high_boost_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
