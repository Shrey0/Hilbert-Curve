import turtle
import random
pencolor = ["orange","blue","green"]
hil = "a"
for _ in range(4):
    seq = ""
    for char in hil:
        if char == "a":
            seq += "-bf+afa+fb-"
        elif char == "b":
            seq += "+af-bfb-fa+"
        else:
            seq += char
    hil = seq
turtle.goto(-650,-350)
for char in hil:

    if char == "f":
        turtle.pencolor(pencolor[random.randrange(0,3)])
        turtle.speed(50)
        turtle.forward(13)
    elif char == "+":
        turtle.right(90)
    elif char == "-":
        turtle.left(90)

turtle.close()