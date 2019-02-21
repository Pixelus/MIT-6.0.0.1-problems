#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:12:49 2018

@author: PixelNew
"""

# Write a program that asks the user to input 10 integers, and then prints the
# largest odd number that was entered. If no odd number was entered, it should
# print a message to that effect.

integers = []

# Asks the user to input 10 integers
for i in range(1, 4):
    print("Enter integer: ")
    integers += input()
    
print(list(integers))

# Prints the largest odd number that was entered
maxInt = max(integers)
print(maxInt)
if(int(maxInt) % 2 == 0):
    print(str(maxInt) + " is the largest odd number from the list.")
else:
    print(str(maxInt) + " is the largest even number from the list.")
