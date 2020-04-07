import turtle


def drawCurveFinal(turtle, l, n):
    turtle.setup(1000, 600)

    if n == 1:
        turtle.forward(l/3)
        turtle.left(60)
        turtle.forward(l/3)
        turtle.right(120)
        turtle.forward(l/3)
        turtle.left(60)
        turtle.forward(l/3)
        return

    drawCurveFinal(turtle,l,n-1)
    turtle.left(60)
    drawCurveFinal(turtle,l,n-1)
    turtle.right(120)
    drawCurveFinal(turtle,l,n-1)
    turtle.left(60)
    drawCurveFinal(turtle,l,n-1)





drawCurveFinal(turtle, 50,3)
turtle.exitonclick()
