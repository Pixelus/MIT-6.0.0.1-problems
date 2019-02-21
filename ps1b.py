#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Wed Nov 7 17:02:11 2018
# @author: PixelNew

###############################################################################
# You decide that you want to start saving to buy a house. You realize you are
# going to have to save for several years before you can afford to make the
# down payment on a house. Write a program to calculate how many months it will
# take you to save up enough money for a down payment.
###############################################################################

# Initialize variables
current_savings = 0.0
r = 0.04
months = 0

# Ask the annual salary to the user
annual_salary = float(input("Enter your annual salary: "))

# Ask the amount % of user salary to saving each month for the down payment
portion_saved = float(input("Enter the percent of your salary to save, as a \
                            decimal:​ "))

# Ask the cost of the user dream home
total_cost = float(input("Enter the cost of your dream home: "))

# Cost needed for a down payment
portion_down_payment = total_cost * 0.25

# Ask the semiannual raise of the user
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

###############################################################################
# Determine how long it will take you to save enough money to make the down
# payment.
###############################################################################

while current_savings < portion_down_payment:
    months += 1
    if(months % 6 == 0):
        annual_salary += (annual_salary / 12) * semi_annual_raise
        print("Jackpot, month is: " + str(months))
    monthly_savings = (annual_salary / 12) * portion_saved
    current_savings += monthly_savings + ((current_savings * r) / 12)
print("Number of months: " + str(months))
