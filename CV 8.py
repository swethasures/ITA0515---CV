import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676298645369.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
