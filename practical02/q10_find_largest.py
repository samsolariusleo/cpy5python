# Filename: q10_find_largest.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that finds the largest integer n where n^3 is less
# than 12000.

# main

# define n
n = 1

# while loop
while n**3 < 12000:
    n = n + 1

# print results
print("The largest integer n for n^3 less than 12000 is " + str(n - 1) + ".")
