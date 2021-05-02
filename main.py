import turtle as t
import random
turtle = t.Turtle()
t.colormode(255)
t.screensize(canvwidth=400, canvheight=400)
turtle.shape("circle")
turtle.pensize(15)
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]

for i in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
