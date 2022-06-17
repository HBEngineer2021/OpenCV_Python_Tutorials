import cv2
import numpy as np
from matplotlib import pyplot as plt

imageName = cv2.imread("../kivy_opencv/img/date_a_live_10th.png", 0)
fig = plt.figure()
plt.hist(imageName.ravel(), 256, [0, 256])
fig.savefig("../kivy_opencv/img/histImage.png")