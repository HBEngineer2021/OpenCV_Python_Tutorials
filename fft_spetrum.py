#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:09:41 2022

@author: user
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# 入力画像
imageName = input("画像名を入力するしてください。\n")
img = cv2.imread("./img/" + imageName, cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()