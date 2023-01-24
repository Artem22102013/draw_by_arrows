import turtle
import random
r = random
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "green", "blue"]
for x in range(100):
    t.pencolor(r.choice(colors))
    t.forward(x)
    t.left(90)
