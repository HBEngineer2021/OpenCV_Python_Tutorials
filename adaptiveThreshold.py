#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:10:36 2022

@author: user
"""

import cv2

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName, cv2.IMREAD_GRAYSCALE)

src = img

maxValue = int(input("最大値を整数値で入力して下さい。\n"))

adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C

thresholdType = cv2.THRESH_BINARY

blockSize = int(input("ブロックサイズを整数値で入力して下さい。\n"))

C = int(input("近傍領域を整数値で入力して下さい。\n"))

def adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C):
    dst = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
    filename = "./img/" + input("画像名を入力するしてください。\n")
    cv2.imwrite(filename, dst)
        
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)