# square.py

import turtle

# make our turtle
pixel = turtle.Turtle()

# buzz makes a square
lines = 0
while lines < 4:
	pixel.forward(150)
	pixel.left(90)
lines = lines + 1

# wait to exit until I've clicked
turtle.exitonclick()
