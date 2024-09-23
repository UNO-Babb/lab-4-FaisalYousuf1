import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(ky, corner):
    #draw big square
    drawSquare(ky, 100)
    
    if corner == 2:
        ky.begin_fill()
        drawSquare(ky, 50)
        ky.end_fill()
    elif corner == 3:
        ky.forward(50)
        ky.begin_fill()
        drawSquare(ky, 50)
        ky.end_fill()
        ky.forward(5)
    elif corner == 4:
        ky.right(90)
        ky.forward(50)
        ky.left(90)
        ky.begin_fill()
        drawSquare(ky, 50)
        ky.end_fill()
        ky.left(90)
        ky.backward(50)
        ky.right(90)
    elif corner == 5:
        ky.forward(100)
        ky.left(90)
        ky.backward(100)
        ky.left(90)
        ky.begin_fill()
        drawSquare(ky, 50)
        ky.end_fill()
        ky.left(90)
        ky.right(90) 
