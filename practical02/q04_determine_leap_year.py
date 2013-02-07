# Filename: q04_determine_leap_year.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that determines whether the input is a leap year.

# main

# prompt for year
year = int(input("Enter year: "))

# check if it is a leap year and return result
if year % 4 == 0:
    print("Leap")
else:
    print("Non-Leap")
