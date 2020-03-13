import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_screen = turtle.Screen()

my_screen.bgcolor('pink')
my_turtle.color('green')
my_turtle.fillcolor('blue')
my_turtle.width(75)
my_turtle.speed(2000)
def recursive_circle(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(90)
        my_turtle.begin_fill()
        my_turtle.circle(height,180)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.circle(height, -180)
        my_turtle.end_fill()
        recursive_circle(x + 10 + height / 2, y + height - 15, height, depth - 1)
        recursive_circle(x + 10 - height / 2, y + height - 15, height, depth - 1)

recursive_circle(0, -200, 100, 5)


my_turtle.color('orange')
my_turtle.fillcolor('yellow')
my_turtle.width(3)
my_turtle.speed(2000)
def recursive_circle(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(90)
        my_turtle.begin_fill()
        my_turtle.circle(height,180)
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.circle(height, -180)
        my_turtle.end_fill()
        recursive_circle(x + 10 + height / 2, y + height - 15, height, depth - 1)
        recursive_circle(x + 10 - height / 2, y + height - 15, height, depth - 1)

recursive_circle(0, -200, 50, 6)

my_screen.exitonclick()