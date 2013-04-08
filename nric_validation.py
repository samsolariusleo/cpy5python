# Filename: nric_validation.py
# Author: Gan Jing Ying
# Created: 20130408
# Modified: 20130408
# Description: Program that checks if the NRIC input is valid.

# import stuff
import re

# define functions
def multiplyweight(n):
    i = 0
    # multiply each digit by their weight
    while i != len(n):
        resultseries.append(n[i] * weightseries[i])
        i = i + 1
    results = 0
    # add them up
    for e in resultseries:
        results = results + int(e)
        resultseries.remove(e)
    return results

def multiplyweight(n):
    results = 0
    for i in range(1,8):
        results = results + int(weightseries[i-1]) * int(n[i-1])
    return results

# define stuff
weightseries = [2, 7, 6, 5, 4, 3, 2]
charseriesST = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
charseriesFG = ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]

# main

# get user information (NRIC)
nricinput = input("Enter NRIC: ")

# check length of the nric
while len(nricinput) != 9:
    print('''Your NRIC should be 9 characters long. Please check your input and
          try again.''')
    nricinput = input("Enter NRIC: ")

# accept some inputs for the first character
firstletter = re.compile("[sSfFgGtT]")

# check first character of the nric
while not firstletter.match(nricinput[0]):
    print('''Your NRIC should start with one of the following characters: S, T,
F or G. Please check your input and try again.''')
    nricinput = input("Enter NRIC: ")

# accept some inputs for the first numeral
firstnumberS = re.compile("[016789]")
firstnumberO = re.compile("[23]")

# check first numeral
if nricinput[0] == "S":
    while not firstnumberS.match(nricinput[1]):
        print('Your NRIC is invalid. Please check your input and try again.')
        nricinput = input("Enter NRIC: ")
else:
    while not firstnumberO.match(nricinput[1]):
        print('Your NRIC is invalid. Please check your input and try again.')
        nricinput = input("Enter NRIC: ")

# perform "weight management"
rangeofno = nricinput[1:-1]
results = multiplyweight(rangeofno)

# for NRICs that start with F or G
if nricinput[0] == "F":
    results = results + 4

# check validation of the last alphabet
results = results % 11
if nricinput[0] == "S" or nricinput[0] == "T":
    if nricinput[-1] != charseriesST[results]:
        print('Your NRIC is invalid. Please check your input and try again.')
    else:
        print('Your NRIC is valid :)')
else:
    if nricinput[-1] != charseriesFG[results]:
        print('Your NRIC is invalid. Please check your input and try again.')
    else:
        print('Your NRIC is valid :)')
