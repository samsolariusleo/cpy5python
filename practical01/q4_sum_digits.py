# Filename: q4_sum_digits.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program that sums up all the digits in an integer.

# main

# prompt for integer
integer = input("Enter integer: ")
sum_of_numbers = 0

# calculate sum
i = 0
while i < len(integer):
    sum_of_numbers = sum_of_numbers + int(integer[i])
    i = i + 1

# return result
print("Sum of numbers = " + str(sum_of_numbers))
