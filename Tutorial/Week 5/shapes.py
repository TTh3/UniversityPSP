import turtle

def draw_triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_star(size):
    turtle.backward(size/2)
    for _ in range(5):
        turtle.forward(size)
        turtle.left(216)
        
def draw_square(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(90) 

