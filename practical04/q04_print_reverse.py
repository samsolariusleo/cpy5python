# Filename: q04_print_reverse.py
# Author: Gan Jing Ying
# Created: 20130225
# Modified: 20130225
# Description: Program that defines a recursive function that reverses the
# digits of an integer n.

# define recursive function
def reverse_int(n):
    if n < 10:
        return n
    else:
        return str(n % 10) + str(reverse_int(n//10))

# main
integer = int(input("Enter integer: "))
print("The reversed integer is: " + reverse_int(integer))
