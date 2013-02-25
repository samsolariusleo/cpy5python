# Filename: q04_sum_series.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130225
# Description: Program that defines a function to compute a series of numbers
# and displays a table of results.

# define variables

# define functions
def m_series(i):
    sum_of_no = 0
    for e in range(1,i+1):
        sum_of_no = sum_of_no + (e/(e+1))
    return sum_of_no

def print_table(i):
    for e in range(1,i+1):
        print("{0:<10}".format(e) + "{0:<10.4f}".format(m_series(e)))

# main
print_table(20)
