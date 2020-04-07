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


def drawCurve2(turtle,l):
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.right(120)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.exitonclick()


def drawCurve3(turtle,l):
    turtle.setup(1000, 400)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.right(120)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)

    turtle.left(60)

    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.right(120)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)

    turtle.right(120)

    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.right(120)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)

    turtle.left(60)

    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)
    turtle.right(120)
    drawCurve(turtle,l)
    turtle.left(60)
    drawCurve(turtle,l)

drawCurve(turtle, 300)
turtle.exitonclick()
