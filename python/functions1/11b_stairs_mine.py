#! /usr/bin/python3

# Write code to draw the staircase
# pattern above.  The modulo operation
# might be useful!

import turtle

def stairs():
    direction   =   -1
    challange   =   turtle.Turtle()
    challange.color("yellow")
    challange.width(5)
    for steps in range(7):
        challange.forward(50)
        challange.right(direction * 90)
        direction   *=  -1

stairs()
