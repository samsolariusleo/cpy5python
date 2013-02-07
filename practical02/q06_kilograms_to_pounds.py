# Filename: q06_kilograms_to_pounds.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that converts kilograms to pounds and creates a table.

# main

# print headers for table
print("{0:10s}".format("Kilograms") + "{0:7s}".format("Pounds"))

# create for loop and print results
for kilograms in range(1,11):
    pounds = kilograms * 2.2
    print("{0:<10}".format(kilograms) + "{0:<7.1f}".format(pounds))
