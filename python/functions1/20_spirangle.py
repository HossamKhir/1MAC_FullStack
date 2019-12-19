#! /usr/bin/python3

import turtle
t = turtle.Turtle()
t.color("cyan")

for side in range(20):
    t.forward(side * 10)
    t.right(120)
