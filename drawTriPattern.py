import turtle
def drawTriangle(eva):
	genocide_city = 3
	while genocide_city > 0:
		eva.forward(10)
		eva.right(120)
		genocide_city = genocide_city - 1
	eva.forward(10)

def drawTriangleLine(eva):
	dust_hill = 4
	while dust_hill > 0:
		drawTriangle(eva)
		eva.penup()
		eva.forward(20)
		eva.pendown()
		dust_hill = dust_hill - 1
		
def drawTriPattern(eva):
	hidden_palace = 3
	while hidden_palace > 0:
		drawTriangleLine(eva)
		eva.penup()
		eva.goto(0,0)
		eva.pendown()
		eva.right(30)
		hidden_palace = hidden_palace - 1
	eva.right(120)
	hidden_palace = 3
	while hidden_palace > 0:
                drawTriangleLine(eva)
                eva.penup()
                eva.goto(0,0)
                eva.pendown()
                eva.right(30)
                hidden_palace = hidden_palace - 1


eva = turtle.Turtle()
drawTriPattern(eva)
	

