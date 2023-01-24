import turtle
t = turtle.Pen()
bgcolor = "black"
colors = ["red", "yellow", "green", "blue"]
for x in range(100):
    t.pencolor(colors%4x)
    t.forward(x)
    t.left(90)
