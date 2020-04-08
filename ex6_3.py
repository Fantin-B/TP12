import turtle
from ex6_2 import *

def drawFullCurve(turtle, l, n):

    drawCurveFinal(turtle,l,n)
    turtle.right(120)
    drawCurveFinal(turtle,l,n)
    turtle.right(120)
    drawCurveFinal(turtle,l,n)
    turtle.right(120)


drawFullCurve(turtle, 50,1)
turtle.exitonclick()
