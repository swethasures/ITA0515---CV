import cv2

img = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306323158.jpg")

wm = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/watermark-logo.png", cv2.IMREAD_UNCHANGED)

h_wm, w_wm, _ = wm.shape

top_y = img.shape[0] - h_wm
left_x = img.shape[1] - w_wm

roi = img[top_y:img.shape[0], left_x:img.shape[1]].copy()  

wm_resized = cv2.resize(wm, (roi.shape[1], roi.shape[0]))

result = cv2.addWeighted(roi, 1, wm_resized[:, :, :3], 0.3, 0)

img[top_y:img.shape[0], left_x:img.shape[1]] = result

cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
