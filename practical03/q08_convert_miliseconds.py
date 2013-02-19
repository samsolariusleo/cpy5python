# Filename: q08_convert_miliseconds.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130219
# Description: Program that converts miliseconds to hours, minutes and seconds.

# define variables

# define functions
def round_down(x):
    position = str(x).find(".")
    if position != -1:
        x = str(x)
        x = x[:position]
    return x

def convert_ms(n):
    seconds = n / 1000
    if seconds > 60:
        minutes = seconds / 60
        seconds = seconds % 60
        if minutes > 60:
            hours = minutes / 60
            minutes = minutes % 60
        else:
            hours = 0
    else:
        hours = 0
        minutes = 0
    return hours, minutes, seconds

# main

# prompt for input
to_be_converted = int(input("Enter miliseconds: "))

# assign values
hours, minutes, seconds = convert_ms(to_be_converted)

# return results
print("Time: " + str(round_down(hours)) + ":" +
      str(round_down(minutes)) + ":" + str(round_down(seconds)))
