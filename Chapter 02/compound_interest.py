# Programming Exercise: Compound Interest Calculator
# 
# Task: Write a program that calculates the ending principal in a bank
# account after compounding the interest.
#
# Requirements:
# 1. Ask the user to enter the starting principal
# 2. Ask the user to enter the annual interest rate (as a percentage)
# 3. Ask the user how many times per year the interest is compounded
# 4. Ask the user for how many years the account will earn interest
# 5. Calculate the ending balance using the compound interest formula:
#    A = P(1 + r/n)^(nt)
#    Where: A = ending amount, P = principal, r = annual interest rate,
#           n = number of times interest is compounded per year, t = time in years
# 6. Display the ending balance formatted as currency
#
# Formula: a = p * (1 + r/n)^(n*t)
# Note: Remember to convert the interest rate from percentage to decimal
#
# Example output: "At the end of 5 years you will have $1,276.28"

principal = float(input("Enter the starting principal: "))
annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
compounds_per_year = int(input("Enter the number of times the interest is compounded per year: "))
years = int(input("Enter the number of years the account will earn interest: "))

amount = principal * (1 + annual_rate / compounds_per_year) ** (compounds_per_year * years)

print(f"At the end of {years} years you will have ${amount:.2f}")