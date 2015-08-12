import cv2
import numpy as np
import copy

img = cv2.imread("CarPlateFull/cp10.jpg")
img_resized = cv2.resize(img, (1280,960))
img_median = cv2.medianBlur(img_resized,1)
# img_median = cv2.bilateralFilter(img_resized,100,75,75)
img_gray = cv2.cvtColor(img_median, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
img_binary = copy.copy(thresh1)

# kernel = np.ones((5,5),np.uint8)
# img_dilated = cv2.dilate(img_binary,kernel,iterations = 4)

img2, contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_countours = copy.copy(img2)

# detector = cv2.SimpleBlobDetector_create()
# keypoints = detector.detect(thresh1)
# params = cv2.SimpleBlobDetector_Params()
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(thresh1, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# idx = 0
# for i in range(len(contours)):
# #     idx += 1
#     cnt = contours[i]
#     x,y,w,h = cv2.boundingRect(cnt)
#     print w, h
#     if (h/w < 1):
#         continue
#     if h<50 or w<20:
#         continue
#     if w*h < 200:
#         continue
#     if w*h > 15000:
#         continue
#     if w>800:
#         continue
#     cv2.rectangle(img_resized,(x,y),(x+w,y+h),(0,255,0),2)
#     roi=img[y:y+h,x:x+w]
#     cv2.imwrite(str(idx) + '.jpg', roi)

for i in range(0, len(contours)):
    cnt = contours[i]
    x,y,w,h = cv2.boundingRect(cnt)
    print w, h
    if (h/w < 1):
        continue
    if h<50 or w<20:
        continue
    if w*h < 200:
        continue
    if w*h > 15000:
        continue
    cv2.rectangle(img_resized,(x,y),(x+w,y+h),(0,255,0),2)

# height = 0
# num = 0
# letters = []
# ht = []
# 
# for (i,cnt) in enumerate(contours):
#     (x,y,w,h) = cv2.boundingRect(cnt)
#     if w*h<200:
# #         cv2.drawContours(thresh1,[cnt],0,(0,0,0),-1)
#         continue
#     if (h/w < 1):
#         continue
#     else:
#         cv2.rectangle(img_resized,(x,y),(x+w,y+h),(0,255,0),2)
#         height = height + h
#         num = num + 1
#         letters.append(cnt)
#         ht.append(h)
# 
# avgh = height/num
# print avgh


# cv2.imshow("plate", img)
# cv2.imshow("resize", img_resized)
# cv2.imshow("gray", img_gray)
cv2.imshow("binary", img_median)
# cv2.imshow("Countours", img_countours)
cv2.imshow('Features', img_resized)
# cv2.waitKey(0)

cv2.waitKey(0)