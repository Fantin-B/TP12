import turtle

def drawCurve(turtle, l):
    turtle.setup(800, 400)

    if l == 0:
        turtle.forward(l/3)
        turtle.left(45)
    turtle.right(60)
    drawCurve(turtle,)


    turtle.exitonclick()
