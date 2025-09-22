# Design Exercise 2: Turtle Graphics - Triangle Pattern
#
# Task: Use turtle graphics to draw a pattern with outer and inner triangles.
#
# Requirements:
# 1. Import the turtle module
# 2. Define named constants for coordinates:
#    - OUTER_TOP_X = 0, OUTER_TOP_Y = 200
#    - INNER_TOP_X = 0, INNER_TOP_Y = 100
#    - BASE_LEFT_X = -100, BASE_LEFT_Y = 0
#    - BASE_RIGHT_X = 100, BASE_RIGHT_Y = 0
# 3. Hide the turtle cursor and raise the pen
# 4. Move to the bottom right corner (BASE_RIGHT_X, BASE_RIGHT_Y)
# 5. Set the fill color to blue and lower the pen
# 6. Draw the outer triangle by connecting:
#    - Bottom right to outer top
#    - Outer top to bottom left
#    - Bottom left to bottom right
# 7. Draw the inner triangle (filled) by connecting:
#    - Bottom right to inner top
#    - Inner top to bottom left
#    - Bottom left to bottom right
#
# Note: Use begin_fill() and end_fill() for the inner triangle
#
# Expected result: An outer triangle outline with a filled inner triangle

import turtle

OUTER_TOP_X, OUTER_TOP_Y = 0, 200
INNER_TOP_X, INNER_TOP_Y = 0, 100
BASE_LEFT_X, BASE_LEFT_Y = -100, 0
BASE_RIGHT_X, BASE_RIGHT_Y = 100, 0

turtle.hideturtle()
turtle.penup()

turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

turtle.fillcolor("blue")
turtle.pendown()

turtle.goto(OUTER_TOP_X, OUTER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

turtle.begin_fill()
turtle.goto(INNER_TOP_X, INNER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.end_fill()

turtle.done()