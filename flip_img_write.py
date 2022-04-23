#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:13:47 2022

@author: user
"""

import cv2

setImage = input()
img = cv2.imread('./img/' + setImage)

def showImage(flipImg, src):
    dest = cv2.flip(flipImg, src)
    saveImg = input()
    cv2.imwrite('./img/' + saveImg + '.png', dest)
    
setSrc = input()
showImage(img, setSrc)

#cv2.waitKey(0)
#cv2.destroyAllWindows()