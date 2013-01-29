# Filename: q02_triangle.py
# Author: Gan Jing Ying
# Created: 20130129
# Modified: 20130129
# Description: Program that calculates perimeter of triangle

# main

# prompt for lengths
side01 = int(input("Enter side 1: "))
side02 = int(input("Enter side 2: "))
side03 = int(input("Enter side 3: "))

# calculate perimeter of triangle
perimeter = side01 + side02 + side03

# check values and return results
if side01+side02 > side03 and side01+side03 > side02 and side02+side03 > side01:
    print("Perimeter = " + str(perimeter))
else:
    print("Invalid triangle!")
