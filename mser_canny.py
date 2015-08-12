import numpy as np
import cv2
import copy

im = cv2.imread('cp5.jpg')

r = 1000.0 / im.shape[1]
dim = (1000, int(im.shape[0] * r))

im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
median_image = cv2.medianBlur(gray_image, 9)
ret,thresh1 = cv2.threshold(median_image,127,255,cv2.THRESH_BINARY)
binary_img = copy.copy(thresh1)

cv2.imshow("binary", thresh1)
cv2.waitKey(0)