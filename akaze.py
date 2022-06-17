import cv2

img = cv2.imread("../kivy_opencv/img/date_a_live_10th.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

akaze = cv2.AKAZE_create()
kp = akaze.detect(gray, None)

dst = cv2.drawKeypoints(gray, kp, None, flags=4)

cv2.imwrite("../kivy_opencv/img/date_a_live_10th_akaze.png", dst)