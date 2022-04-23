#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 13:45:04 2022

@author: user
"""

import cv2

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName)

rgb = cv2.split(img)

blue = rgb[0]
green = rgb[1]
red = rgb[2]

def rgbImage(src):
    saveImage = input("画像名を入力するしてください。\n")
    cv2.imwrite("./img/" + saveImage, src)
    
rgbImage(blue)
rgbImage(green)
rgbImage(red)