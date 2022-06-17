import cv2
import numpy as np

cap = cv2.VideoCapture("../kivy_opencv/img/らき☆すた×頭文字D_Trim_Trim_Trim.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow("frame", fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()