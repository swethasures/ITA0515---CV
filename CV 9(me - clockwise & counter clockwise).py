import cv2
import numpy as np

def rotate_image(image_path, degrees):
    original_image = cv2.imread(image_path)

    height, width = original_image.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degrees, 1)

    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))

    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "C:/Users/HP/Pictures/Pictures/vivo v 23/Facebook/FB_IMG_1676298839279.jpg"
rotate_image(image_path, 90)  # Rotate clockwise by 90 degrees
rotate_image(image_path, -90)  # Rotate counter-clockwise by 90 degrees

