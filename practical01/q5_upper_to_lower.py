# Filename: q5_upper_to_lower.py
# Author: Gan Jing Ying
# Created: 20130122
# Modified : 20130122
# Description: Program that converts an upper-case letter to
# a lower-case letter.

# main

# prompt user for letter
letter = input("Enter letter: ")

# convert letter and return result
while letter == letter.upper():
    print("Error! The letter is an upper-case!")
    letter = input("Enter letter: ")
print("Converted letter: " + letter.upper())


# When the user inputs a non-upper-case letter, the user will have to re-input
# the letter. This cycle goes on until the user inputs a lower-case letter.
