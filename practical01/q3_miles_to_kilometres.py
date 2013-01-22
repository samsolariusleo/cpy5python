# Filename: q3_miles_to_kilometres.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program that converts a value from miles to kilometres.

# main

# prompt for distance in miles
miles = float(input("Enter distance in miles: "))

# convert miles to kilometers
kilometres = miles * 1.60934

# return result
print("Distance in Kilometres: {0:.3f}".format(kilometres))
