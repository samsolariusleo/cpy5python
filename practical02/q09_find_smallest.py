# Filename: q09_find_smallest.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that finds the smallest integer n such that n^2 is
# greater than 12000.

# main

# define n
n = 1

# while loop
while n**2 < 12000:
    n = n + 1

#print result
print("The smallest integer n for n^2 greater than 12000 is " + str(n))
