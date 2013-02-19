# Filename: q03_find_gcd.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130219
# Description: Program that defines a function to find the greatest common
# divisor of two numbers.

# define function
def smaller(m,n):
    if m > n:
        smaller_no = n
    else:
        smaller_no = m
    return m,n,smaller_no
    
def find_gcd(m,n,d):
    while m % d != 0 or n % d != 0:
        d = d - 1
    return d

def gcd(m,n):
    m,n,d = smaller(m,n)
    gcd = find_gcd(m,n,d)
    return gcd
    
# main

##integer01 = int(input("Enter first integer: "))
##integer02 = int(input("Enter second integer: "))
##
##print("The Greatest Common Divisor is " + str(gcd(integer01,integer02)))

print(gcd(24, 16))
print(gcd(255, 25))

