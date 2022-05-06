#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 00:08:26 2022

@author: user
"""

import cv2

imageName = input("画像名を入力して下さい。\n")

img = cv2.imread("./img/" + imageName, cv2.IMREAD_GRAYSCALE)

thresh = 200

maxval = 255

threshType = cv2.THRESH_BINARY

def threshold(img, thresh, maxval, threshType):
    ret, dst = cv2.threshold(img, thresh, maxval, threshType)
    outputFileName = input("保存します。画像名を入力して下さい。\n")
    cv2.imwrite("./img/" + outputFileName, dst)
    cv2.imshow("thresh_show", dst)

threshold(img, thresh, maxval, threshType)

cv2.waitKey(0)
cv2.destroyAllWindows()