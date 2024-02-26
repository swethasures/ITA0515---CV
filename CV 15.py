import cv2
import numpy as np

img1 = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306323158.jpg")
img2 = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676298754715.jpg")

pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])

H, _ = cv2.findHomography(pts1, pts2)

dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
