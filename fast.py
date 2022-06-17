import cv2
import numpy as np
from matplotlib import pyplot as plt

# 画像の読み込み
img = cv2.imread("../kivy_opencv/img/date_a_live_10th.png")

# FAST関数
fast = cv2.FastFeatureDetector_create()

# キーポイント
kp = fast.detect(img, None)
dst = cv2.drawKeypoints(img, kp, None, color=(255, 0, 0), flags=4)

cv2.imwrite("../kivy_opencv/img/date_a_live_10th_fast.png", dst)
