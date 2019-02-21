#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:12:49 2018

@author: PixelNew
"""

# Replace the comment in the following code with a while loop.

numXs = int(input('How many times should I print the letter X? ')) 
toPrint = ''

# concatenate X to toPrint numXs times
while (numXs):
    toPrint = "X" * numXs
    print(toPrint)
    numXs = 0
