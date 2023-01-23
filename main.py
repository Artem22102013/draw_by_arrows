import turtle
t = turtle.Pen()
def f():
    t.forward(50)
def l():
    t.left(90)
def r():
    t.right(90)
while True:
    t.onkeypress(f, "Up")
    t.onkeypress(l, "Left")
    t.onkeypress(r, "Right")
