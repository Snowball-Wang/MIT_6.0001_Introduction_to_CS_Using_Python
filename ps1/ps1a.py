#!/usr/bin/env python3
#*******************************************************
#       Filename: ps1a.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Solution to problem set 1 Part A
#       Created on: 2018-10-14 17:10:49
#*******************************************************
# Input the starting annual salary
annual_salary = float(input('Enter your annual salary: '))

# Input the portion of salary to be saved
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

# Input the cost of your dream home
total_cost = float(input('Enter the cost of your dream home: '))

# Initialize parameters
current_savings = 0
portion_down_payment = 0.25
r = 0.04
months = 0

# Calculate the months
while current_savings <= total_cost * portion_down_payment:
    current_savings += (current_savings * r + annual_salary * portion_saved) / 12
    months += 1

print("Number of months: ", months)
