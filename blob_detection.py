import numpy as np
import cv2
import copy

im = cv2.imread('cp2.jpg')
r = 1000.0 / im.shape[1]
dim = (1000, int(im.shape[0] * r))
im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh1,kernel,iterations = 4)

cv2.imshow("binary", thresh1)
cv2.imshow("dilation", dilation)
cv2.waitKey(0)