import cv2
import numpy as np

img = cv2.imread("../kivy_opencv/img/date_a_live_10th.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp = sift.detect(gray, None)

dst = cv2.drawKeypoints(gray, kp, None, flags=4)

cv2.imwrite("../kivy_opencv/img/date_a_live_10th_SIFT.png", dst)

