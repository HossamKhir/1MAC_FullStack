#! /usr/bin/python3

import turtle
import random

mood = random.choice(["happy", "sad", "angry", ''])

riley = turtle.Turtle()
riley.width(5)

# Add your code here.
if mood == "happy":
    riley.color("yellow")
elif mood == "sad":
    riley.color("blue")
elif mood == 'angry':
    riley.color('red')
else:
    riley.color("grey")

for side in range(5):
    riley.forward(100)
    riley.right(144)
