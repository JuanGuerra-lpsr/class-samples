import turtle
eva = turtle.Turtle()
def windowsLogo(eva):
	balloon_park = 4
	eva.color('red')
	eva.left(90)
	eva.forward(50)
	eva.right(90)
	eva.forward(50)
	eva.color('blue')
	eva.right(90)
	eva.forward(50)
	eva.backward(50)
	eva.left(90)
	eva.forward(50)
	eva.right(90)
	eva.forward(50)
	eva.color('green')
	eva.right(90)
	eva.forward(50)
	eva.backward(50)
	eva.left(90)
	eva.forward(50)
	eva.right(90)
	eva.forward(50)
	eva.color('yellow')
	while balloon_park > 0:
		eva.forward(50)
		eva.right(90)
		balloon_park = balloon_park - 1

def carnival_night(eva):
	pixel = 5
	while pixel > 0:
		windowsLogo(eva)
		eva.right(45)
		eva.penup()
		eva.forward(50)
		eva.pendown()
		eva.right(45)
		pixel = pixel - 1

carnival_night(eva)
