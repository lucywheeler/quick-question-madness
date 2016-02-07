import turtle

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["green", "purple", "red", "white"]
for x in range(10000):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(161)
