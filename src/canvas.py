import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()


# This function draws a box by drawing each side of the square and using the fill function
def draw_box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
	

boxSize = 8

#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)


def draw(pixels, palette):
    for i in range (0,len(pixels)):
        for j in range (0,len(pixels[i])):
            myPen.color(palette[pixels[i][j]])
            draw_box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180) 
        myPen.forward(boxSize*len(pixels[i]))
        myPen.setheading(0)
        myPen.pendown()
