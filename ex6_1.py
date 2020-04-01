import turtle

def drawCurve(turtle, l):
    turtle.setup(800, 400)

    turtle.forward(l/3)
    turtle.left(60)
    turtle.forward(l/3)
    turtle.right(120)
    turtle.forward(l/3)
    turtle.left(60)
    turtle.forward(l/3)


    turtle.exitonclick()

drawCurve(turtle, 300)
