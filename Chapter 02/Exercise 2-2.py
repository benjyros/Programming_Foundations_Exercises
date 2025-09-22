# Programming Exercise 2-2: Sales Prediction
#
# Task: Write a program that calculates the projected profit for a company.
#
# Requirements:
# 1. Ask the user to enter the projected sales amount
# 2. Calculate the projected profit using a 23% profit margin
# 3. Display the projected profit formatted to 2 decimal places
#
# Formula: profit = sales * 0.23
#
# Example:
# Enter the projected sales: 1000
# The projected profit is 230.00

sales = float(input("Enter the projected sales: "))
profit = sales * 0.23
print(f"The projected profit is {profit:.2f}")