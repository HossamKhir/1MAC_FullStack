#! /usr/bin/python3

import turtle

order   =   turtle.Turtle()

def square_side():
    order.forward(100)
    order.right(90)
    
order.color("red")
square_side()
order.color('orange')
square_side()
order.color('yellow')
square_side()
order.color("green")
square_side()
