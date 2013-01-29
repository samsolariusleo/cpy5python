# Filename: q03_determine_grade.py
# Author: Gan Jing Ying
# Created: 20130129
# Modified: 20130129
# Description: Program that determines the grades based on the score.

# main

# prompt for score
score = int(input("Enter score: "))

# grades data
grade_boundary = [[100, 70], [69, 60], [59, 55], [54, 50], [49, 45], [44, 35], [34, 0]]
grade = ["A", "B", "C", "D", "E", "S", "U"]

# determine grade and return results
i = 0
while i < len(grade_boundary):
    if grade_boundary[i[0]] < score < grade_boundary[i[1]]:
        print(grade[i])
    i = i + 1
