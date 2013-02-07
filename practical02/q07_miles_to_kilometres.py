# Filename: q07_miles_to_kilometres.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that converts miles to kilometres and kilometres to miles
# before printing the results 

# main

# print headers
print("{0:6s}".format("Miles") + "{0:11s}".format("Kilometres") +
      "{0:11s}".format("Kilometres") + "{0:6s}".format("Miles"))

# define for loop
for miles in range(1,11):
    convert_to_kilo = miles * 1.609
    convert_to_miles = (miles + 3) * 5 / 1.609
    print("{0:<6}".format(miles) + "{0:<11.3f}".format(convert_to_kilo) +
          "{0:<11}".format((miles + 3) * 5) +
          "{0:<6.3f}".format(convert_to_miles))
