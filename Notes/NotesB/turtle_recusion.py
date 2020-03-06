import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_screen = turtle.Screen()
my_screen.bgcolor('blue')


my_turtle.fillcolor('purple')
my_turtle.begin_fill()

my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

my_screen.clear()
my_turtle.speed(200)
my_turtle.up()
my_turtle.goto(200, 200)
my_turtle.down()
my_turtle.setheading(200)
#my_turtle.fillcolor('green')

my_turtle.color('violet')

def feather_flower():
    for i in range (1,10):
        my_turtle.speed(250)
        for i in range (13):
            my_turtle.forward(35)
            my_turtle.left(180)
            my_turtle.forward(35)
            my_turtle.left(185)
            my_turtle.forward(45)
            my_turtle.left(180)
            my_turtle.forward(45)
            my_turtle.left(185)
            my_turtle.forward(50)
            my_turtle.left(180)
            my_turtle.forward(50)
            my_turtle.left(185)

        my_turtle.forward(60)
        my_turtle.right(35)
        my_turtle.forward(75)

feather_flower()
my_turtle.up()
my_turtle.goto(50, 200)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(-100, 200)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(-100,50)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(-100,-100)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(50,-100)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(200,-100)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(200,50)
my_turtle.down()

feather_flower()
my_turtle.up()
my_turtle.goto(200,200)
my_turtle.down()

feather_flower()
my_screen.clear()




'''
def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2, depth / 2)
        my_turtle.down()
        my_turtle.goto(-width / 2, height / 2)
        my_turtle.goto(-width / 2, -height / 2)
        my_turtle.goto(width / 2, -height / 2)
        my_turtle.goto(width / 2, height / 2)
        recursive_rect(width / 2, height / 2, depth -1)

recursive_rect(200, 300, 4)

'''

my_screen.exitonclick()