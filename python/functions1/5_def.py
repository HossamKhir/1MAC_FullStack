#! /usr/bin/python3

import turtle

polygon =   turtle.Turtle()

# Write a function here that creates a
# turtle and draws a shape with it.
def draw_polygon(sides=3, length=100, width=5, speed=0, colour="blue", angle=120):
    polygon.color(colour)
    polygon.width(width)
    polygon.speed(speed)
    for side in range(sides):
        polygon.forward(length)
        polygon.right(angle)
    
# Call the function multiple times.

for colour in ["red", "orange", "blue"]:
    for pattern in range(6):
        draw_polygon(3,100,5,0,colour,120)
        polygon.right(15)
    polygon.right(30)
