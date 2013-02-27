# Filename: q08_find_uppercase.py
# Author: Gan Jing Ying
# Created: 20130227
# Modified: 20130227
# Description: Program that defines a recursive function that returns the number
# of uppercase letters in a string defined by the user.

# define recursive function
def find_num_uppercase(string):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']
    if len(string) != 1:
        if string[0] in uppercase:
            return True + find_num_uppercase(string[1:])
        else:
            return False + find_num_uppercase(string[1:])
    else:
        if string[0] in uppercase:
            return True
        else:
            return False

# main
string = input("Enter string: ")
print("The number of uppercase letters in this string is " +
      str(find_num_uppercase(string)) + ".")
