import turtle, random
colors =["red","green","blue","orange","purple","pink",]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(110)
    painter.right(35)
    painter.left(70)
    painter.setposition(0, 0)
