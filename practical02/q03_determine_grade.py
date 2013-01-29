# Filename: q03_determine_grade.py
# Author: Gan Jing Ying
# Created: 20130129
# Modified: 20130129
# Description: Program that determines the grades based on the score.

# main

# prompt for score
score = int(input("Enter score: "))

# check for validity of score
while score < 0 or score > 100:
    print("Invalid! Score must be between 0 - 100!")
    score = int(input("Enter score: "))

# grades data
grade_boundary = [[100, 70, "A"], [69, 60, "B"], [59, 55, "C"],
                  [54, 50, "D"], [49, 45, "E"], [44, 35, "S"], [34, 0, "U"]]

# determine grade and return results
for e in grade_boundary:
    if e[0] >= score >= e[1]:
        print(e[2])

