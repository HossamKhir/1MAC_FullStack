#! /usr/bin/python3

import turtle
t = turtle.Turtle()
t.width(5)
t.color("limegreen")

for step in range(21):
  t.forward(10)  # just one!

  # Alternate turning left and right.
  if step % 2 == 0:
    t.left(90)
  else:
    t.right(90)

t.hideturtle()
