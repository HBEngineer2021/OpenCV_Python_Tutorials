#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:37:43 2022

@author: user
"""

import cv2
import numpy as np

# 入力画像
imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName, cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]], np.float32)

k = 9

def sharpenFilter(img, kernel, k):

    ddepth = -1

    # 平均化フィルタ
    average = cv2.filter2D(img, ddepth, kernel)
    
    # diffをk倍してから、入力画像を加算する（鮮鋭化フィルタ）
    sharpen = img + (img - average) * k
    
    outputImage = input("画像名を入力するしてください。\n")
    
    cv2.imwrite("./img/" + outputImage, sharpen)

sharpenFilter(img, kernel, k)
    
def sharpenKernel(k: int):
    return np.array([[-k/9, -k/9, -k/9],
                     [-k/9, 1 + 8/9 * k, -k/9],
                     [-k/9, -k/9, -k/9]], np.float32)

kernel = sharpenKernel(9)

sharpen = cv2.filter2D(img, -1, kernel)

outputImage = input("画像名を入力するしてください。\n")
    
#cv2.imwrite("./img/" + outputImage, sharpen)