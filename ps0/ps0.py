#!/usr/bin/env python3
#*******************************************************
#       Filename: ps0.py
#       Author: Snowball Wang
#       Mail: wjq1996@mail.ustc.edu.cn
#       Description: Solution to problem set 0
#       Created on: 2018-10-11 09:24:48
#*******************************************************
from numpy import log2

# Ask the user to enter a number "x"
x = int(input('Enter number x: '))
# Ask the user to enter a number "y"
y = int(input('Enter number y: '))
# Print out number "x", raised to the power "y"
print("x**y: ", x**y)
# Print out the log (base 2) of "x"
print("log(x): ",log2(x))

