#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:02:12 2022

@author: user
"""

import cv2

setImageName = input("参照する画像名を入力して下さい。\n")
img = cv2.imread("./img/" + setImageName)

def resizeImage(setImage, scale1, scale2, width, height):
     dst = cv2.resize(setImage, (int(width * scale1), int(height * scale2)))
     saveFileName = input("保存する画像名を入力してください。\n")
     cv2.imwrite("./img/" + saveFileName + ".png", dst)
     

scale1 = 0.5
scale2 = 0.5
width = img.shape[0]
height = img.shape[1]

resizeImage(img, scale1, scale2, width, height)