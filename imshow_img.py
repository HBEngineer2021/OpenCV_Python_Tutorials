#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:45:21 2022

@author: user
"""

import cv2

# 画像ファイル名を入力する。
fileName = input()

# 入力したファイル名から画像データを詠み込む。
img = cv2.imread('./img/' + fileName)

# 読み込んだファイル名を表示できる様にウィンドウを作成する。
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()