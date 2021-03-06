# Filename: q07_find_largest.py
# Author: Gan Jing Ying
# Created: 20130227
# Modified: 20130227
# Description: Program that defines a recursive function that returns the
# largest integer in an array defined by the user.

# define recursive function
def find_largest(alist):
    if len(alist) != 1:
        if alist[0] > alist[1]:
            alist.remove(alist[1])
            return find_largest(alist)
        else:
            alist.remove(alist[0])
            return find_largest(alist)
    else:
        return alist[0]

# define functions
def create_array():
    array = []
    no_of_int = int(input("Enter No. of Integers in Your Array: "))
    for i in range(0, no_of_int):
        array.append(int(input("Enter integer: ")))
    return array

# main
array = create_array()
print("The largest integer in your array is " + str(find_largest(array)) + ".")
