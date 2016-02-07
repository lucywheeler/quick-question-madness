import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["purple", "blue", "pink", "red", "magenta", "cyan"]
for x in range (100000000):
  t.pencolor(colors[x%6])
  t.circle (x)
  t.left(91)
