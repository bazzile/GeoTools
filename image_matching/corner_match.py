import os
import cv2
import numpy as np

src_dir = r"C:\Users\lobanov\PycharmProjects\GeoTools\image_matching\img"
template_img = r"C:\Users\lobanov\PycharmProjects\GeoTools\image_matching\match_small.jpg"

for dirpath, dirnames, filenames in os.walk(src_dir):
    for filename in filenames:
        if filename.lower().endswith('.bmp'):
            src_image_path = os.path.join(dirpath, filename)
            print(src_image_path)

            # preventing cv2-specific errors with Unicode
            stream = open(src_image_path, "rb")
            bytes_obj = bytearray(stream.read())
            numpyarray = np.asarray(bytes_obj, dtype=np.uint8)

            # reading image in grayscale
            # src_image_obj_gray = cv2.imread(src_image_path, 0)
            src_image_obj_gray = cv2.imdecode(numpyarray, 0)
            # getting src_image dimensions
            full_w, full_h = src_image_obj_gray.shape[::-1]
            # print(full_w, full_h)

            # setting the ROI
            ul_x1, ul_y1 = 0, 0
            ul_x2, ul_y2 = int(full_w/4), int(full_h/4)
            # src_image_obj_gray = src_image_obj_gray[0:0+int(full_w/4), 0:0+int(full_h/4)]

            template_image_obj_gray = cv2.imread(template_img, 0)
            w, h = template_image_obj_gray.shape[::-1]

            # insert ROI here
            result = cv2.matchTemplate(src_image_obj_gray, template_image_obj_gray, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            locations = np.where(result >= threshold)

            ul, ur, ll, lr = zip(*locations[::-1])
            dx, dy = 4, 4

            for match_coord in ul, ur, ll, lr:
                match_coord = list(match_coord)
                center_coord = [match_coord[0] + dx, match_coord[1] + dy]
                print(match_coord, center_coord)

            #
            # for point in zip(*locations[::-1]):
            #     # print(point)
            #
            #     cv2.rectangle(
            #         img=src_image_obj_gray, pt1=point, pt2=(point[0] + w - 1, point[1] + h - 1), color=100, thickness=1)
            #
            # cv2.imwrite(os.path.join(dirpath, 'detected.png'), src_image_obj_gray)
