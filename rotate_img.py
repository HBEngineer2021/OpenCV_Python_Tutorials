#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:10:30 2022

@author: user
"""

import cv2

imageName = input("画像名を入力して下さい。\n")

img = cv2.imread("./img/" + imageName)

height = img.shape[0]
width = img.shape[1]

center = (int(width/2), int(height/2))
angle = float(input("angleを入力。\n")) 
scale = float(input("scaleを入力。\n"))

def rotate(center, angle, scale):
    affinTransition = cv2.getRotationMatrix2D(center, angle, scale)
    dst = cv2.warpAffine(img, affinTransition, (width, height))
    outputImage = input("出力画像名を入力して下さい。\n")
    cv2.imwrite("./img/" + outputImage, dst)
    
rotate(center, angle, scale)