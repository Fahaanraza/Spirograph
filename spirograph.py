from turtle import Turtle, Screen, pendown
import random
import turtle
dino = Turtle()
dino.shape("turtle")
dino.color("navy")
dino.speed("fastest")
turtle.colormode(255)
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colour=(r,g,b)
    return random_colour
for i in range(0,361,5):
    dino.setheading(i)
    dino.pencolor(random_colour())
    dino.circle(100)
screen = Screen()
screen.exitonclick()
