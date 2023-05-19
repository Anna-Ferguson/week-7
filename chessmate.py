import turtle

def drawRectangle(width, height, x, y):
        w = width/10
        h = height/10
        turtle.pu()
        turtle.setposition(x, y)
        turtle.pd()
        for i in range(2):
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)

        turtle.end_fill()
        turtle.done()

def drawAllRectangles(width, height,x, y):
    w = width/10
    h = height/10
    for i in range(5):
        for i in range(4):
            drawRectangle(width, height, x, y)
            turtle.pu()
            turtle.forward(w * 2)
            turtle.pd()
        turtle.pu()
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
        turtle.forward(w*10)
        turtle.right(180)

        turtle.done()

def drawChessboard(x, y, width=50,height=50):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    drawAllRectangles(width, height, x, y)
    turtle.done()

def main():
    x = int(input("Enter your starting positions  X: ")) ; y= int(input("Y: "))
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))

    startX = 250
    startY = 250
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=width)
    elif width == "":
        drawChessboard(startX, startY, height=height)
    else:
        drawChessboard(startX, startY, width, height)
    
    

main()
