#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Write a program that examines three variables—x, y, and z—and prints the 
#largest odd number among them. If none of them are odd, it should print a 
#message to that effect.

x = input("Enter a number x: ")
x = int(x)
y = input("Enter a number y: ")
y = int(y)
z = input("Enter a number z: ")
z = int(z)

# Test to find the largest odd number
# x is odd ?
if int(x % 2 == 0):
    oddX = True
else:
    oddX = False
    
### y is odd ?  
if y % 2 == 0:
    oddY = True
else:
    oddY = False

### z is odd ?    
if z % 2 == 0:
    oddZ = True
else:
    oddZ = False   

while (x != 0 and y != 0 and z != 0):
    if (oddX == True and oddY == True and oddZ == True):
        if ((x > y and x > z) or (x > z and y < z)):
            print("The largest odd number is: " + str(x))
            break
        elif ((x > y and x < z) or (x < y and y < z)):
            print("The largest odd number is: " + str(z))
            break
        elif ((x < y and y > z) or (x < y and z < y)):
            print("The largest odd number is: " + str(y))
            break
