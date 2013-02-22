# Filename: q02_display_pattern.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130219
# Description: Program that defines a function to display a pattern.

# define functions
def no_of_char(n):
    if n <= 9:
        char = n + n
        return char
    elif 9 < n <= 99:
        char = 9 * 1
        more_char = n - char
        char = char + more_char * 2 + n
        return char
    elif 99 < n <= 999:
        char = 9 * 1
        more_char = n - char
        char = char + 90 * 2
        more_char = n - 99
        char = char + more_char * 3 + n
        return char
    else:
        print("Error!")

def display_pattern(n, char):
    answer = ""
    formatting = "{0:>%ds}"%char
    for i in range(0,n):
        answer = " " + str(i) + answer
        print(formatting.format(answer))
        
# main

# print warning
print('''Warning: This program works fine for all values between 0 and 999
      inclusive. However, if the value is too big, the pattern displayed may
      not appear complete due to lack of space on the screen. Nevertheless,
      the program works fine.''')
print() # line break

# prompt for integer
integer = int(input("Enter number: "))

# check for integer == 0
while integer == 0:
    print("Error! Number must be at least 1!")
    integer = int(input("Enter number: "))

# display pattern
display_pattern(integer, no_of_char(integer))



