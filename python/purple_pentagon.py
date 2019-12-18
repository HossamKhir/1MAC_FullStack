#! /usr/bin/python3

import turtle

mary        =   turtle.Turtle()
whatever    =   'purple'
steps       =   100
angles      =   72
sides       =   [1, 2, 3, 4, 5]

mary.color(whatever)

for side in sides:
    mary.forward(steps)
    mary.right(angles)
