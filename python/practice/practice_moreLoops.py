#! /usr/bin/python3

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between

for color in ["red", "orange", "yellow"]:
    amy.color(color)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()

amy.hideturtle()
# amy.forward(50)
# amy.penup()
# amy.forward(50)
# amy.pendown()

# amy.forward(50)
# amy.penup()
# amy.forward(50)
# amy.pendown()

