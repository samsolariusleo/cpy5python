# Filename: q06_determine_prime.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130222
# Description: Program that defines a function to check for prime numbers and
# prints out the first 1000 prime numbers in rows of 10.

# define variables
import math

# define functions
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

### test function
##print(is_prime(11))
##print(is_prime(9))

# main

# Need to make use of function is_prime(n), formatting, while loops (maybe),
# for loops (don't think so, but perhaps...), len()

