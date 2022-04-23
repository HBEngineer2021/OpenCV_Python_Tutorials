#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:58:23 2022

@author: user
"""

import cv2

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName)

def bitwise(img):
    dst = cv2.bitwise_not(img)
    outputImage = input("画像名を入力するしてください。\n")
    cv2.imwrite("./img/" + outputImage, dst)
    
bitwise(img)