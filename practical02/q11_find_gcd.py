# Filename: q11_find_gcd.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program to find the greatest common divisor of two integers.

# main

# prompt user for the two integers
integer_one = int(input("Enter first integer: "))
integer_two = int(input("Enter second integer: "))

# find out which is the smaller of integer_one and integer_two
if integer_one > integer_two:
    d = integer_two
elif integer_one < integer_two:
    d = integer_one
else:
    print("The greatest common divisor is " + str(integer_one) + ".")
    exit()

# find greatest divisor
while integer_one % d != 0 or integer_two % d != 0:
    d = d - 1

# return results
print("The greatest common divisor is " + str(d) + ".")
