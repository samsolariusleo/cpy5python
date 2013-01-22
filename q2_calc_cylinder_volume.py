# Filename: q2_calc_cylinder_volume.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program that calculates the volume of a cylinder.

radius = int(input("Enter radius: "))
length = int(input("Enter length: "))

from math import pi
area = radius * radius * pi
volume = area * length

print("Volume: {0:.3f}".format(volume))
