#! /usr/bin/python3

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw a red line
amy.color("red")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)
amy.pendown()

# Draw an orange line
amy.color("orange")
amy.forward(50)

# Move forward without drawing anything
amy.penup()
amy.forward(50)
amy.pendown()

# Draw a yellow line
amy.color("yellow")
amy.forward(50)
amy.hideturtle()
