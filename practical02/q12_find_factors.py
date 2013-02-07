# Filename: q12_find_factors.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that displays the smallest factors of an integer.

# main

# prompt for integer
integer = int(input("Enter integer: "))

# define smallest factor
factor = 2

# define a list
list_of_factors = []

# find factors
while factor < integer:
    while integer % factor != 0:
        factor = factor + 1
    list_of_factors.append(factor)
    integer = integer//factor

# return results
print("The smallest factors are " + str(list_of_factors)[1:-1] + ".")
