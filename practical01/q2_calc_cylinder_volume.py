# Filename: q2_calc_cylinder_volume.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program that calculates the volume of a cylinder.

# main

# prompt for radius
radius = float(input("Enter radius: "))

# prompt for length
length = float(input("Enter length: "))

# calculate volume
from math import pi
area = radius * radius * pi
volume = area * length

# return value of volume
print("Volume: {0:.3f}".format(volume))
