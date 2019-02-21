#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:26:11 2018

@author: PixelNew
"""

# Write a program that asks the user to enter an integer and prints two 
# integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the
# integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

pwr = 3
root = 0

# Asks the user to enter an integer
print("Enter an integer: ", end = '')
number = int(input())

# Prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is 
# equal to the integer entered by the user
if(pwr == 1):
    root = number
else:
    root = number / pwr
print("Pwr is equal to " + str(pwr) + ", root is equal to " + str(root))
result = root * pwr
print("Integer is equal to " + str(number) + " and pwr * root is equal to " + str(result))

# If no such pair of integers exists, it should print a message to that effect
if(int(root) * int(pwr) != number):
    print("No pair of integers exists for this number!")
else:
    print("Matches!")
