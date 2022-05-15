#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:57:53 2022

@author: user
"""

import cv2
import numpy as np

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("./img/" + "grayscale_" + imageName, img)

def weightedAverageMultiply3(img):
    
    ddepth = -1
    
    # カーネルサイズ【3 × 3】の場合
    kernel = np.array([[1,2,1],
                       [2,4,2],
                       [1,2,1]], np.float32)/16
    
    dst = cv2.filter2D(img, ddepth, kernel)
    
    outputImage = input("画像名を入力するしてください。\n")
    
    cv2.imwrite("./img/" + outputImage, dst)
    
def weightedAverageMultiply5(img):
    
    ddepth = -1
    
    # カーネルサイズ【5 × 5】の場合
    kernel = np.array([[1,4,6,4,1],
                       [4,16,24,16,4],
                       [6,24,36,24,6],
                       [4,16,24,16,4],
                       [1,4,6,4,1]], np.float32)/256
    
    dst = cv2.filter2D(img, ddepth, kernel)
    
    outputImage = input("画像名を入力するしてください。\n")
    
    cv2.imwrite("./img/" + outputImage, dst)
    
#weightedAverageMultiply3(img)
#weightedAverageMultiply5(img)