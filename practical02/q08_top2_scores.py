# Filename: q08_top2_scores.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that outputs the top 2 scorers among a group of students
# from a set of scores.

# main

# prompt for number of students
number_of_students = int(input("Enter number of students: "))
print()

# define empty lists for names and scores
names = []
scores = []

# prompt for names and scores
while number_of_students > 0:
    student_name = input("Enter name of student: ")
    student_score = input("Enter score of student (in 3 digits): ")
    names.append(student_name)
    scores.append(student_score)
    number_of_students = number_of_students - 1
    print()
    
# find the top scorer
position = scores.index(max(scores))
highest_score = scores.pop(position)
top_scorer = names.pop(position)

# find the second top scorer
position = scores.index(max(scores))
second_highest_score = scores.pop(position)
second_top_scorer = names.pop(position)

# print results
print()
print("The top scorer is " + top_scorer + " with a score of " +
      str(highest_score) + ".")
print("The second highest scorer is " + second_top_scorer + " with a score of "
      + str(second_highest_score) + ".")
      
