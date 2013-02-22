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

def print_matrix():
    integer = 2 # initialize number
    for i in range(0,100):
        for e in range(0,10):
            while is_prime(integer) == False:
                integer = integer + 1
            print("{0:>5}".format(str(integer)), end=" ")
            integer = integer + 1
        print()

# main
print("The first 1000 Prime Numbers are: ")
print()
print("<Start Prime Numbers>")
print_matrix()
print("<End Prime Numbers>")
