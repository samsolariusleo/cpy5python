# Filename: q02_triangle.py
# Author: Gan Jing Ying
# Created: 20130129
# Modified: 20130129
# Description: Program that calculates perimeter of triangle

# main

# prompt for lengths
length01 = int(input("Enter side 1: ")
length02 = int(input("Enter side 2: ")
length03 = int(input("Enter side 3: ")

# calculate perimeter of triangle
perimeter = length01 + length02 + length03

# check values and return results
if length01 + length02 > length03:
  print("Perimeter = " + str(perimeter))
elif length01 + length03 > length02:
  print("Perimeter = " + str(perimeter))
elif length02 + length03 > length01:
  print("Perimeter = " + str(perimeter))
else:
  print("Invalid triangle!")


