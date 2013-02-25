# Filename: q06_sum_digits.py
# Author: Gan Jing Ying
# Created: 20130225
# Modified: 20130225
# Description: Program that defines a recursive function whcih computes the sum
# of the digits in an integer n.

# define recursive function
def sum_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + (sum_digits(n//10))

# main
integer = int(input("Enter integer: "))
print("Sum of Digits = " + str(sum_digits(integer)))
