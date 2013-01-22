# Filename: q2_calc_cylinder_volume.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program that computes the volume of a cylinder.

# main

# prompt user to input radius of circular base
radius = int(input("Enter radius: "))

# prompt user to input length of cylinder
length = int(input("Enter length: ")

# calculate volume of cylinder
from math import *
area = radius * radius * pi
volume = area * length

# return volume
print(volume)
