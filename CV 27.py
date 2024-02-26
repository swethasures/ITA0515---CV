import cv2

main_img = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676306323158.jpg")

insert_img = cv2.imread("C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/logo cv image.png")

top_left_y = 100
top_left_x = 200
bottom_right_y = 400
bottom_right_x = 500

cropped_region = main_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

insert_img_resized = cv2.resize(insert_img, (bottom_right_x - top_left_x, bottom_right_y - top_left_y))

main_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = insert_img_resized

cv2.imshow("Result", main_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
