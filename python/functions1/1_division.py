#! /usr/bin/python3

import turtle

# Set the number of sides here.
sides = 5

# Set the length of a side here.
length = 100

t = turtle.Turtle()
t.color("orange")
for side in range(sides):
    t.forward(length)
    t.right(360 / sides)
    # On the line above, replace the
    # value 72 with an arithmetic
    # expression that uses the
    # 'sides' variable.

