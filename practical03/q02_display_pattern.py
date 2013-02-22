# Filename: q02_display_pattern.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130219
# Description: Program that defines a function to display a pattern.

# define functions
def no_of_char(n):
    if n <= 9:
        char = n
    elif 9 < n <= 99:
        char = 9 * 1
        more_char = n - char
        char = char + more_char * 2
    elif 99 < n <= 999:
        char = 9 * 1
        more_char = n - char
        char = char + more_char * 2
        more_char = n - char
        char = char + more_char * 3
    else:
        print("Error!")

# main
integer = int(input("Enter number: "))

# check for integer == 0
while integer == 0:
    print("Error! Number must be at least 1!")
    integer = int(input("Enter number: "))
