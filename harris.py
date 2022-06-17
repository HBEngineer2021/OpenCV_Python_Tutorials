import cv2
import numpy as np

img = cv2.imread("../kivy_opencv/img/date_a_live_10th.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gary = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()] = [0, 0, 255]

cv2.imwrite("../kivy_opencv/img/date_a_live_10th_harris.png", img)