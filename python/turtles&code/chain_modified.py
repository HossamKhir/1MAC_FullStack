#! /usr/bin/python3

import turtle

links = [1, 2, 3, 4, 5, 6]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    weaver.forward(10)
    # Draw a hexagon.
    for side in sides:
        weaver.right(60)
        weaver.forward(30)

    # Scoot over to the next link.
#     weaver.penup()
#     weaver.forward(20)
#     weaver.pendown()
    weaver.right(-60)

weaver.hideturtle()

