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
im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contour_img = copy.copy(im2)


for i in range(0, len(contours)):
    cnt = contours[i]
    x,y,w,h = cv2.boundingRect(cnt)
       
    if (h/w < 1):
        continue
    if h<90 or w<30:
        continue

    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Features', im)


# cv2.imshow("img",im)
# cv2.imshow("gray", gray_image)
# cv2.imshow("median", median_image)
# cv2.imshow("binary", binary_img)
# cv2.imshow("countour", contour_img)
# cv2.imshow("draw", im3)
cv2.waitKey(0)


