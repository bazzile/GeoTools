import os
import cv2
import numpy as np


src_image_path = r'/Users/vasily/!MyFiles/Coding/PycharmProjects/GeoTools/image_matching/4-А-1-эл.bmp'

# reading image in grayscale
src_image_obj_gray = cv2.imread(src_image_path, 0)
# getting src_image dimensions
full_w, full_h = src_image_obj_gray.shape[::-1]
print(full_w, full_h)

# setting the ROI
ul_x1, ul_y1 = 0, 0
ul_x2, ul_y2 = int(full_w/4), int(full_h/4)
# src_image_obj_gray = src_image_obj_gray[0:0+int(full_w/4), 0:0+int(full_h/4)]

template_image_obj_gray = cv2.imread('match_small.jpg', 0)
w, h = template_image_obj_gray.shape[::-1]

# insert ROI here
result = cv2.matchTemplate(src_image_obj_gray, template_image_obj_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
location = np.where(result >= threshold)

print(location)
for point in zip(*location[::-1]):
    print(point)
    cv2.rectangle(
        img=src_image_obj_gray, pt1=point, pt2=(point[0] + w - 1, point[1] + h - 1), color=100, thickness=1)

cv2.imwrite('OUT.png', src_image_obj_gray)
