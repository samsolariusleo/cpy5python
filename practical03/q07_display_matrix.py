# Filename: q07_display_matrix.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130222
# Description: Program that defines a function that displays a square matrix
# of random values (either 0 or 1).

import random

# define functions
def print_matrix(n):
    for i in range(0, n): # rows
        for k in range(0, n): # columns
            print(random.randint(0,1), end=" ")
        print()

# main
integer = int(input("Enter matrix length: "))
print_matrix(integer)
