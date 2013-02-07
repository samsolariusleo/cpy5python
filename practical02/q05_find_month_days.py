# Filename: q05_find_month_days.py
# Author: Gan Jing Ying
# Created: 20130207
# Modified: 20130207
# Description: Program that displays number of days in the month of a particular
# year.

# main

# prompt for month
month = int(input("Enter month: "))

# prompt for year
year = int(input("Enter year: "))

# define list of months
allmonths = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

# define list of days
alldays = ["31", "28", "31", "30", "31", "30",
           "31", "31", "30", "31", "30", "31", "29"]

# check if month is feb
# if month is feb, then check if year is leap year
# if both are true, days is 29
# else, days are normal

if month == 2 and year % 4 == 0:
    print(allmonths[month-1] + " " + str(year) + " has " + alldays[-1] +
          " days")
else:
    print(allmonths[month-1] + " " + str(year) + " has " + alldays[month-1] +
          " days")
