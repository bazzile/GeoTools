import os
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


os.chdir(os.path.dirname(os.path.realpath(__file__)))
src_image = r"C:\Users\lobanov\PycharmProjects\GeoTools\image_matching\4-А-1-эл.bmp"
img = Image.open(src_image)
print(os.path.splitext(os.path.basename(src_image))[0])
temp_jpg = 'temp_image' + '.jpg'
img.convert('RGB').save(temp_jpg, 'jpeg')
# img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_rgb = cv2.imread(temp_jpg)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('opencv-template-for-matching.jpg', 0)
template = cv2.imread('match_small.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w - 1, pt[1] + h - 1), (255, 0, 0), 1)

# cv2.imshow('Detected', img_rgb)
# cv2.waitKey(0)

# plt.imshow(img_rgb, interpolation='nearest')
# plt.show()

cv2.imwrite('OUT.png', img_rgb)
os.remove(temp_jpg)
