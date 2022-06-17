import cv2
import numpy as np

img = cv2.imread("../kivy_opencv/img/utawarerumono.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5))

dst = cv2.dilate(img, kernel, iterations = 3)

cv2.imwrite("../kivy_opencv/img/utawarerumono_dilate1.jpg", dst)