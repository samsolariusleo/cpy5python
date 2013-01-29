# Filename: q7_generate_payroll.py
# Author: Gan Jing Ying
# Created: 20130123
# Modified: 20130128
# Description: Program that prints a payroll statement from given information.

# main

# prompt for name
name = input("Enter name: ")

# prompt for weekly working hours
hours_weekly = float(input("Enter number of hours worked weekly: "))

# prompt for hourly pay rate
pay_rate = float(input("Enter hourly pay rate($): "))

# prompt for CPF contribution rate
contribution = float(input("Enter CPF contribution rate(%): "))

# calculate gross pay
gross_pay = hours_weekly * pay_rate

# calculate CPF contribution
calc_contribution = gross_pay * (contribution / 100)

# calculate net pay
net_pay = gross_pay - calc_contribution

# convert int and float to str
gross_pay = "%0.2f" % gross_pay
calc_contribution = "%0.2f" % calc_contribution
net_pay = "%0.2f" % net_pay
# The "%0.2f" function converts a number (int or float_ to a 2 s.f. number
# Learned this online because the formatting thing I learned in class
# didn't seem to work in this code... O.O
hours_weekly = str(hours_weekly)
pay_rate = str(pay_rate)
gross_pay = str(gross_pay)
contribution = str(contribution)
calc_contribution = str(calc_contribution)
net_pay = str(net_pay)

# return results
print("~~~~~ PAYROLL IS AS FOLLOWS ~~~~~")
print("Payroll statement for " + name)
print("Number of hours worked in week: " + str(hours_weekly))
print("Hourly pay rate: " + str(pay_rate))
print("Gross pay = $" + str(gross_pay))
print("CPF contribution at " + str(contribution) + " = $" + str(calc_contribution))
print("Net pay = $" + str(net_pay))
