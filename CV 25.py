import cv2
import numpy as np

a = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306300126.jpg")

lap = np.array([0, 1, 0, 1, -4, 1, 0, 1, 0]).reshape(3, 3)

a1 = cv2.filter2D(a, -1, lap)

a2 = np.uint8(a1)

cv2.imshow("Laplacian Result", a2)
cv2.waitKey(0)
cv2.destroyAllWindows()

sharpening_filter = np.array([-1, -1, -1, -1, 9, -1, -1, -1, -1]).reshape(3, 3)

a3 = cv2.filter2D(a, -1, sharpening_filter)

a4 = np.uint8(a3)

cv2.imshow("Sharpening Result", a4)
cv2.waitKey(0)
cv2.destroyAllWindows()
