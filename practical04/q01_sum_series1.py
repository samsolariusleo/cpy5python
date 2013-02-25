# Filename: q01_sum_series1.py
# Author: Gan Jing Ying
# Created: 20130225
# Modified: 20130225
# Description: Program that defines a recursive function that computes the sum
# of a series of numbers.

# define recursive function
def sum_series1(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return 1/i + sum_series1(i-1)

# main
integer = int(input("Enter integer: "))
print("Sum of Series = " + str(sum_series1(integer)))
