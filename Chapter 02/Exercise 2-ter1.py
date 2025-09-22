# Programming Exercise 2-ter1: Decimal to Binary Converter
#
# Task: Write a program that converts a decimal number to binary format.
#
# Requirements:
# 1. Ask the user to enter a decimal number
# 2. Convert the decimal number to binary using different formatting methods
# 3. Display the binary number in different formats:
#    - Basic binary format
#    - 8-bit binary format with leading zeros
#    - Using f-string formatting
#    - Using format() function
#
# Methods to demonstrate:
# - "{0:b}".format(dec_number) - basic binary
# - '{0:08b}'.format(dec_number) - 8-bit with leading zeros
# - f'{dec_number:08b}' - f-string formatting
# - format(dec_number, "08b") - format function
#
# Example:
# Enter a decimal number: 42
# 101010
# 00101010
# 00101010
# 00101010

while True:
	try:
		dec_number = int(input("Enter a decimal number: "))
		break
	except ValueError:
		print("Invalid input. Please enter a whole number (integer).")

print(f"""
{"{0:b}".format(dec_number)}
{"{0:08b}".format(dec_number)}
{f'{dec_number:08b}'}
{format(dec_number, '08b')}
""")
