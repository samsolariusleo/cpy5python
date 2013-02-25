# Filename: q02_sum_series2.py
# Author: Gan Jing Ying
# Created: 20130225
# Modified: 20130225
# Description: Program that defines a recursive function that computes the sum
# of a series.

# define recursive function
def sum_series2(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1/3
    else:
        return i/(2*i + 1) + sum_series2(i-1)

# main
integer = int(input("Enter integer: "))
print("Sum of Series = " + str(sum_series2(integer)))
