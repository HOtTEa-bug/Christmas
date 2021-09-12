# Christmas Tree

from turtle import *
from shapes import *
from random import randint

speed(0)

window = turtle.Screen()
window.bgcolor("#69D9FF")

# Set the start position and width of the tree
y= -100
width= 240

# Tree Trunk
draw_rectangle(turtle, "brown", -15, y - 40, 30, 40)

# TREE
while width>20:
    width = width - randint(20,30)
    height = randint(15,35)
    x = 0 - width / 2
    draw_rectangle(turtle,"green", x, y, width, height)
    y = y + height


# Star
draw_star(turtle, "yellow", 4, y, 20)

#message
penup()
color("red")
goto(-100, -180)
write("Merry Christmas", font=("Comic Sans", 20, "bold"))

hideturtle()
