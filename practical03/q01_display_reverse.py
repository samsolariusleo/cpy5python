# Filename: q1_display_reverse.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130219
# Description: Program that defines a function which returns the reverse of a
# number given by the user.

# define variables
i = 0
numbers = []

# define a procedure
def reverse_int(n):
    return str(n)[::-1]

# main
integer = input("Enter integer: ")
print("Reverse = " + reverse_int(integer))

