# Turtle Revisit Week 10

import turtle

def drawTriangle(size=100):
    for num in range(3):
        turtle.forward(size)
        turtle.left(120)
# drawTriangle(300)

def drawStar(size=100):
    for num in range(5):
        turtle.forward(size)
        turtle.left(216)

drawStar()