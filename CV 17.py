import cv2
img = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306280869.jpg") 
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) 
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
