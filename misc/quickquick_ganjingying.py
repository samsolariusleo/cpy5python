# Filename: quickquick_ganjingying.py
# Author: Gan Jing Ying
# Created: 20130422
# Modified: 20130422
# Description: Program that allows user to input up to five integers between
# 0 - 100, adds them into MyArray and then sorts them using quick sort.

# define functions
def quick_sort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        less = []
        great = []

        for i in array[1:]:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                great.append(i)

        less = quick_sort(less)
        great = quick_sort(great)
    return less + [pivot] + great

def check_ascii(n):
    if ord(n) < 48 or ord(n) > 57:
        n = 101
        return n
    else:
        return n

def get_input(array):
    start = True
    while start:
        start = False
        num = input("Enter integer between 0 - 100: ")
        num = int(check_ascii(num))
        if num >= 0 and num <= 100:
            array.append(num)
        else:
            print("Error! Please enter a proper integer between 0 - 100!")
            start = True
    return array

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
            

# define variables
MyArray = []
error = True

# main

# get number of inputs
print("How many integers would you like to sort today?")
print("You may only enter up to 5 integers.")
print()
n = int(input("Enter number of inputs: "))

# check the number of inputs
while n < 0 or n > 5:
    print("Error! This program only accepts up to 5 integer inputs. Please try again.")
    n = int(input("Enter number of inputs: "))

# allow users to input up to 5 integers between 0 - 100
for i in range(0,n):
    get_input(MyArray)

# sort array
MyArray = quick_sort(MyArray)
print()
print("Your sorted array is " + str(MyArray) + ".")
print()

# searching through the array using binary search
searchyes = input("Would you like to perform binary search on your array? (Enter 'y' to search, any key to exit)")
if searchyes == 'y':
    yes = True
else:
    yes = False
    exit()
while yes:
    yes = False
    # allow user to input search key
    target = input("Enter search key: ")
    while ord(target) < 48 or ord(target) > 57:
        target = input("Enter search key: ")
    target = int(target)
    pos = binary_search(MyArray, target)
    print()
    if pos == -1:
        print("Your search key was not found in MyArray.")
        searchyes = input("Would you like to try again? (Enter 'y' to search, any key to exit)")
        if searchyes == 'y':
            yes = True
        else:
            yes = False
            exit()
    else:
        print("SUCCESS! Your search key was found at position " + str(pos) + ".")
        searchyes = input("Would you like to try again? (Enter 'y' to search, any key to exit)")
        if searchyes == 'y':
            yes = True
        else:
            yes = False
            exit()
