#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:38:22 2022

@author: user
"""

import cv2
import numpy as np

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName)

a = int(input("カーネルサイズaを入力。\n"))
b = int(input("カーネルサイズbを入力。\n"))

ksize = (a, b)

def cv2_blur(img, ksize):
    dst = cv2.blur(img, ksize)
    outputImage = input("画像名を入力するしてください。\n")
    cv2.imwrite("./img/" + outputImage, dst)

def cv2_filter2d(img):
    
    ddepth = -1
    
    # カーネルサイズ【3 × 3】の場合
    kernel = np.array([[1/9,1/9,1/9],
                       [1/9,1/9,1/9],
                       [1/9,1/9,1/9]])
    
    dst = cv2.filter2D(img, ddepth, kernel)
    
    outputImage = input("画像名を入力するしてください。\n")
    
    cv2.imwrite("./img/" + outputImage, dst)

#cv2_blur(img, ksize)
cv2_filter2d(img)