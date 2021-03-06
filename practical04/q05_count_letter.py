# Filename: q05_count_letter.py
# Author: Gan Jing Ying
# Created: 20130227
# Modified: 20130227
# Description: Program that defines a recursive function that finds the number
# of occurrences of a specific character in a string.

# define recursive function
def count_letter(string, character):
    if len(string) != 1:
        if string[0] == character:
            return True + count_letter(string[1:],character)
        else:
            return False + count_letter(string[1:],character)
    else:
        if string[0] == character:
            return True
        else:
            return False

# main
string = input("Enter what you want to search in: ")
character = input("Enter what you want to search for: ")

print("The number of occurrences of '" + character + "' in '" + string + "' is " + 
      str(count_letter(string, character)) + ".")
