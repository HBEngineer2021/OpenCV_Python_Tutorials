#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:38:22 2022

@author: user
"""

import cv2

imageName = input("画像名を入力するしてください。\n")

img = cv2.imread("./img/" + imageName)

a = int(input("カーネルサイズaを入力。\n"))
b = int(input("カーネルサイズbを入力。\n"))

ksize = (a, b)

def blur(img, ksize):
    dst = cv2.blur(img, ksize)
    outputImage = input("画像名を入力するしてください。\n")
    cv2.imwrite("./img/" + outputImage, dst)

blur(img, ksize)