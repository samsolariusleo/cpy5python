# Filename: q05_compute_series.py
# Author: Gan Jing Ying
# Created: 20130219
# Modified: 20130225
# Description: Program that defines a function to compute a series and prints
# a table of results.

# define variables

# define functions
def m_series(i):
    sum_of_no = 0 # initialize the sum of numbers
    for e in range(1,i+1,2):
        sum_of_no = sum_of_no + 1/((2 * e) - 1) - 1/((2 * e + 1))
    sum_of_no = sum_of_no * 4
    return sum_of_no

def print_series(i):
    for e in range(1,i+1):
        print("{0:<5}".format(e) + "{0:<15.11f}".format(m_series(e)))

# main
print_series(19)
