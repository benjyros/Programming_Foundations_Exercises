# Programming Exercise 2-6: Installment Loan Calculator
#
# Task: Write a program that calculates the cost of an installment loan.
#
# Requirements:
# 1. Ask the user to enter the purchase amount
# 2. Ask the user to enter the desired number of installments
# 3. Calculate the final purchase amount (add 5% to original amount)
# 4. Calculate the cost per installment
# 5. Display the final purchase amount, number of installments, and cost per installment
#
# Formulas:
# - finalAmount = amount * 1.05 (adds 5% to original amount)
# - instalmentCost = finalAmount / instalments
#
# Example:
# Enter the purchase amount: 1000
# Enter the desired number of instalments: 12
# 
# Final purchase amount: 1050.00
# Number of instalments: 12
# Cost per instalment: 87.50

amount = float(input("Enter the purchase amount: "))
instalments = int(input("Enter the desired number of instalments: "))

finalAmount = amount * 1.05  # adds 5% to original amount
instalmentCost = finalAmount / instalments

print(f"""
Final purchase amount: {finalAmount:.2f}
Number of instalments: {instalments}
Cost per instalment: {instalmentCost:.2f}
""")