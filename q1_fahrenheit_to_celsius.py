# Filename: q1_fahrenheit_to_celsius.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified: 20130122
# Description: Program to convert a temperature reading from Fahrenheit to Celsius.

#main

# prompt to get temperature
temperature = float(input("Enter temperature (Fahrenheit): "))

# calculate temperature in Celsius
temperature = (5/9) * (temperature - 32)

# display result
print(temperature)
