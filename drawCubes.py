import turtle
gaz = turtle.Turtle()
zim = turtle.Turtle()
gaz.speed(8)
zim.speed(1)

def drawRhombus1(gaz):
	doom = 2
	gaz.color("purple")
	gaz.right(30)
	gaz.begin_fill()
	while doom > 0:
		gaz.left(60)
		gaz.forward(20)
		gaz.left(120)
		gaz.forward(20)
		doom = doom - 1
	gaz.end_fill()
def drawRhombus2(zim):
	zim.right(30)
	zim.color("green")
	zim.fillcolor("green")
	zim.begin_fill()
	zim.right(60)
	zim.forward(20)
	zim.right(120)
	zim.forward(20)
	zim.right(60)
	zim.forward(20)
	zim.right(120)
	zim.forward(20)
	zim.end_fill()
	zim.right(60)
	zim.color("red")
	zim.fillcolor("red")
	zim.begin_fill()
	zim.forward(20)
	zim.left(120)
	zim.forward(20)
	zim.left(60)
	zim.forward(20)
	zim.end_fill()
	zim.end_fill()
def drawRhombusline1(gaz):
	prof_membrane = 3
	while prof_membrane > 0:
		drawRhombus1(gaz)
		gaz.left(30)
		gaz.penup()
		gaz.forward(32)
		gaz.pendown()
		prof_membrane = prof_membrane - 1
	gaz.penup()
	gaz.backward(116)

drawRhombusline1(gaz)
drawRhombus2(zim)
zim.backward(10)
zim.right(90)
zim.penup()
zim.forward(18)
zim.pendown()
drawRhombus2(zim)
zim.backward(10)
zim.right(90)
zim.penup()
zim.forward(18)
zim.pendown()
drawRhombus2(zim)
