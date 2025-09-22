# Design Exercise 3: Turtle Graphics - Connected Squares
#
# Task: Use turtle graphics to draw two squares connected by lines.
#
# Requirements:
# 1. Import the turtle module
# 2. Define named constants for all square coordinates:
#    - Top square coordinates (top-left, top-right, bottom-left, bottom-right)
#    - Bottom square coordinates (top-left, top-right, bottom-left, bottom-right)
# 3. Hide the turtle cursor and raise the pen
# 4. Draw the top square by connecting its corners
# 5. Draw the bottom square by connecting its corners
# 6. Connect the corners between the two squares:
#    - Bottom square bottom-right to top square top-left
#    - Bottom square top-right to top square top-right
#    - Bottom square bottom-left to top square bottom-left
#
# Note: Use penup() and pendown() to move between drawing areas
#
# Expected result: Two squares with connecting lines forming a 3D-like effect

import turtle

TOP_SQUARE_TL, TOP_SQUARE_TR, TOP_SQUARE_BL, TOP_SQUARE_BR = (-50, 50), (50, 50), (-50, -50), (50, -50)
BOTTOM_SQUARE_TL, BOTTOM_SQUARE_TR, BOTTOM_SQUARE_BL, BOTTOM_SQUARE_BR = (-130, -30), (-30, -30), (-130, -130), (-30, -130)

turtle.hideturtle()
turtle.penup()

# Draw top square
turtle.goto(TOP_SQUARE_TL)
turtle.pendown()
turtle.goto(TOP_SQUARE_TR)
turtle.goto(TOP_SQUARE_BR)
turtle.goto(TOP_SQUARE_BL)
turtle.goto(TOP_SQUARE_TL)
turtle.penup()

# Draw bottom square
turtle.goto(BOTTOM_SQUARE_TL)
turtle.pendown()
turtle.goto(BOTTOM_SQUARE_TR)
turtle.goto(BOTTOM_SQUARE_BR)
turtle.goto(BOTTOM_SQUARE_BL)
turtle.goto(BOTTOM_SQUARE_TL)
turtle.penup()

# Connect corners
turtle.goto(BOTTOM_SQUARE_TL)
turtle.pendown()
turtle.goto(TOP_SQUARE_TL)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_BR)
turtle.pendown()
turtle.goto(TOP_SQUARE_BR)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_TR)
turtle.pendown()
turtle.goto(TOP_SQUARE_TR)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_BL)
turtle.pendown()
turtle.goto(TOP_SQUARE_BL)
turtle.penup()

turtle.done()