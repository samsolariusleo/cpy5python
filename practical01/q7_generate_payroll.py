# Filename: q7_generate_payroll.py
# Author: Gan Jing Ying
# Created: 20130123
# Modified: 20130123
# Description: Program that prints a payroll statement from given information.

# main

# prompt for name
name = input("Enter name: ")

# prompt for weekly working hours
hours_weekly = int(input("Enter number of hours worked weekly: "))

# prompt for hourly pay rate
pay_rate = int(input("Enter hourly pay rate($): "))

# prompt for CPF contribution rate
contribution = int(input("Enter CPF contribution rate(%): "))

# calculate gross pay
gross_pay = hours_weekly * pay_rate

# calculate CPF contribution
calc_contribution = gross_pay * (contribution / 100)

# calculate net pay
net_pay = gross_pay - calc_contribution

# return results
print("Payroll statement for " + name)
print("Number of hours worked in week: " + str(hours_weekly))
print("Hourly pay rate: " + str(pay_rate))
print("Gross pay = $" + str(gross_pay))
print("CPF contribution at " + str(contribution) + " = $" + str(calc_contribution))
print("Net pay = $" + str(net_pay))
