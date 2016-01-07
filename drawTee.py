import turtle

def drawTee(Eva):
	Eva.forward(200)
	Eva.backward(50)
	Eva.left(90)
	Eva.forward(50)
	Eva.backward(100)
	Eva.forward(50)
	Eva.right(90)
	Eva.backward(150)

def drawFourTees(Eva):
	drawTee(Eva)
	Eva.left(90)
	drawTee(Eva)
	Eva.left(90)
	drawTee(Eva)
	Eva.left(90)
	drawTee(Eva)
#make your turtle down here and pass it to the appropriate places
Eva = turtle.Turtle()
drawFourTees(Eva)
turtle.exitonclick()
