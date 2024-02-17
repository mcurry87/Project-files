# Michael Curry
# Create a stop sign

import turtle
import math

turtle.speed(0)
turtle.color("white")
turtle.bgcolor("black")
turtle.shape("triangle")
turtle.pensize(2)

def rec(width, height):
    turtle.color("white", "gray")       # sets the outline color and the fill color
    turtle.begin_fill()                 # beings the fill process
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()                   # ends the fill process

def oct(len):
    turtle.width(4)
    turtle.color("white", "red")    # sets outline color and fill color
    turtle.begin_fill()             # begins the fill of the shape
    for i in range(8):
        turtle.forward(len)
        turtle.left(45)
    turtle.end_fill()               # ends the fill process



def move(len):
    turtle.penup()
    turtle.back(len)
    turtle.pendown()

def stop(len):
    oct(len)
    move(len * -3/8)
    rec(len * 1/5, len * 2)
    turtle.penup()
    turtle.color("white")
    turtle.setpos(40, 55)     # sets position for text within the stop sign. need to figure out a loop for this
    turtle.write("STOP", False, align="center", font=("impact", 50, "bold"))
    turtle.penup()

stop(75)
move(250)
stop(55)

turtle.hideturtle()

turtle.Screen () .exitonclick()
