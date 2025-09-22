# Programming Exercise: Grapevine Calculator
#
# Task: Write a program that calculates the number of grapevines that can be planted in a vineyard row.
#
# Requirements:
# 1. Ask the user to enter the length of the row in feet
# 2. Ask the user to enter the amount of space used by an end-post assembly in feet
# 3. Ask the user to enter the distance between each vine in feet
# 4. Calculate the number of vines that can be planted
# 5. Display the result formatted to 1 decimal place
#
# Formula: v = (r - 2 * e) / s
# Where:
# - v = number of vines
# - r = length of the row in feet
# - e = space used by an end-post assembly in feet
# - s = distance between each vine in feet
#
# Note: The formula accounts for end-post assemblies at both ends of the row
#
# Example:
# Enter the length of the row, in feet: 100
# Enter the amount of space, in feet, used by an end-post assembly: 5
# Enter the distance, in feet, between each vine: 3
# You have enough space for 30.0 vines.

row_len = float(input("Enter the length of the row in feet: "))
end_post_space = float(input("Enter the amount of space used by an end-post assembly in feet: "))
vine_distance = float(input("Enter the distance between each vine in feet: "))

num_vines = (row_len - 2 * end_post_space) / vine_distance

print(f"You have enough space for {num_vines:.1f} vines.")