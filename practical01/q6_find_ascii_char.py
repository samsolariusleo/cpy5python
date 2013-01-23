# Filename: q6_find_ascii_char.py
# Author: Gan Jing Ying
# Created: 20130123
# Modified: 20130123
# Description: Program that converts an ASCII code to its corresponding
# character.

# main

# prompt for ASCII code
code = int(input("Enter ASCII code: "))

# prevent out of range error
while int(code) < 0 or int(code) > 127:
    print("Error! Out of range!")
    code = int(input("Enter ASCII code: "))

# convert code to character
character = chr(code)
# By the way, I learnt this step from checking out tutorials online.
# it wasn't easy to find an answer to this... considering how little
# knowledge I have of python... :D


# return result
print("Character is: " + character)
