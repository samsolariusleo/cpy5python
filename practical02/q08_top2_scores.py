# Filename: q08_top2_scores.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that outputs the top 2 scorers among a group of students
# from a set of scores.

# main

# prompt for number of students
number_of_students = int(input("Enter number of students: "))

# define empty lists for names and scores
names = []
scores = []

# prompt for names and scores
while number_of_students > 0:
    student_name = input("Enter name of student: ")
    student_score = input("Enter score of student: ")
    
    # append the names and scores into the lists
    
    names = names.append(student_name)
    scores = scores.append(student_score)
    number_of_students = number_of_students - 1
    
# find the top scorer

# find the second top scorer

# print results
