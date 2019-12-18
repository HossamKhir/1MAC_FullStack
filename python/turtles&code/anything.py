#! /usr/bin/python3

import turtle

rainbow =   ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
roygbiv =   turtle.Turtle()
roygbiv.width(5)
roygbiv.penup()
roygbiv.back(150)
roygbiv.pendown()

for colour in rainbow:
    roygbiv.color(colour)
    roygbiv.forward(50)
    roygbiv.right(60)
    
roygbiv.penup()
roygbiv.forward(200)
roygbiv.pendown()
    
for colour in rainbow:
    roygbiv.color(colour)
    for star in range(5):
        roygbiv.forward(50)
        roygbiv.right(144)
    
    roygbiv.penup()
    roygbiv.right(60)
    roygbiv.forward(50)
    roygbiv.pendown()
    
roygbiv.hideturtle()    
