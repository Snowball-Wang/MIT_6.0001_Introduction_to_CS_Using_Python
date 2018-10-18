#!/usr/bin/env python3
#*******************************************************
#       Filename: ps1/ps1c.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Solution to ps1, Part C
#       Created on: 2018-10-18 09:11:48
#*******************************************************

# Input the starting annual salary
annual_salary = float(input('Enter the starting salary: '))

# Initialize some parameters
total_cost = 1000000.0
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0

# Calculate best savings rate and steps in bisection search
low = 0
high = 10000
mid = (low + high) / 2.0
epsilon = 100.0
bisection_times = 0

while abs(current_savings - down_payment) >= epsilon:
    current_savings = 0
    annual_salary_reset = annual_salary
    for month in range(1,37):
        current_savings += (current_savings * r + annual_salary_reset * mid /10000.0) / 12
        if month % 6 == 0:
            annual_salary_reset = annual_salary_reset * (1 + semi_annual_raise)

    if current_savings > down_payment:
        high = mid
    else:
        low = mid
    mid = (high + low) / 2.0
    bisection_times += 1
    if bisection_times >= 15:
        break

# Judge whether bisection_times reaches the limit of bisection.
# If not, print out the step in bisection search, Otherwise print
# the required statement.
if bisection_times < 15:
    print("Best savings rate: %0.4f" %(mid/10000.0))
    print("Step in bisection search: ", bisection_times)
else:
    print("It is not possible to pay the down payment in three years.")
