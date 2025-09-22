# Programming Exercise 2-9: Circle Calculator
#
# Task: Write a program that calculates the area and circumference of a circle.
#
# Requirements:
# 1. Ask the user to enter the radius of a circle
# 2. Calculate the area of the circle
# 3. Calculate the circumference of the circle
# 4. Display both results formatted to 2 decimal places
#
# Formulas:
# - area = π * radius²
# - circumference = 2 * π * radius
#
# Note: Use math.pi for the value of π
#
# Example:
# Enter radius of circle: 5
# 
# Area of circle: 78.54
# Circumference of circle: 31.42

import math

radius = float(input("Enter radius of circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"""
    Area of circle: {area:.2f}
    Circumference of circle: {circumference:.2f}
    """)