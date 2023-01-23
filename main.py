import turtle
t = turtle.Pen()
def f():
    t.forward(50)
def l():
    t.left(90)
def r():
    t.right(90)
while True:
    t.onkey(f, "Up")
    t.onkey(l, "Left")
    t.onkey(r, "Right")
