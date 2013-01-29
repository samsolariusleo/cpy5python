# Filename: q01_check_even.py
# Author: Gan Jing Ying
# Created: 20130129
# Modified: 20130129
# Description: Program that reads an integer and checks if it is even.

# main

# prompt for integer
integer = int(input("Enter number: "))

# check if integer is even
if integer % 2 == 1:
  print(str(integer) + " is odd")
else:
  print(str(integer) + " is even")
