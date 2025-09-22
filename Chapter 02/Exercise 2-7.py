# Programming Exercise 2-7: Miles per Gallon Calculator
#
# Task: Write a program that calculates miles per gallon for a car.
#
# Requirements:
# 1. Ask the user to enter the miles driven
# 2. Ask the user to enter the gallons of fuel used
# 3. Calculate the miles per gallon
# 4. Display the result formatted to 2 decimal places
#
# Formula: mpg = miles / gallons
#
# Example:
# Enter the miles driven: 350
# Enter the gallons of fuel used: 15
# You used 23.33 miles per gallon.

miles = float(input("Enter the miles driven: "))
gallons = float(input("Enter the gallons of fuel used: "))

miles_per_gallon = miles / gallons

print(f"You used {miles_per_gallon:.2f} miles per gallon.")