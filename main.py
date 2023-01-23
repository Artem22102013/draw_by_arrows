import turtle
t = turtle.Pen()
def f():
    t.forward(50)
def l():
    t.left(90)
def r():
    t.right(90)
while True:
    turtle.onkeypress(f, "Up")
    turtle.onkeypress(l, "Left")
    turtle.onkeypress(r, "Right")
