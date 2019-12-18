#! /usr/bin/python3

import turtle

builder = turtle.Turtle()
builder.color("red")
builder.width(5)

# Copy the angles variable here!
angles = [-90, 0, 0, -90,\
          135, 0, 0, 0, \
          90, 0, 0, 0,\
          135, -90, 0, 0,\
          90, 0, 0, 0]

for angle in angles:
    # Turn right, then go forward 25.
    # (How far to turn?
    #  Use the angle variable!)
    builder.right(angle)
    builder.forward(25)
