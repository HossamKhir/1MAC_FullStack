#! /usr/bin/python3

import turtle
jack = turtle.Turtle()
jack.color("yellow")

def draw_square(length = 100):
    for side in range(4):
        jack.forward(length)
        jack.right(90)
        
# draw_square()

jack.penup()
jack.back(150)
jack.pendown()

draw_square()
jack.forward(100)
draw_square()
jack.forward(100)
draw_square()

jack.speed(0)
jack.back(50)

for square in range(80):
    draw_square(50)
    jack.forward(5)
    jack.left(5)
