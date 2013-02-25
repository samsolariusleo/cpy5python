# Filename: q03_find_gcd.py
# Author: Gan Jing Ying
# Created: 20130225
# Modified: 20130225
# Description: Program that defines a recursive function that finds the greatest
# common divisor between two numbers.

# define recursive function
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

# main
print(gcd(24, 16))
print(gcd(255, 25))

### extra (uncomment for testing)
##integer1 = int(input("Enter first integer: "))
##integer2 = int(input("Enter second integer: "))
##print("Greatest Common Divisor = " + str(gcd(integer1, integer2)))
