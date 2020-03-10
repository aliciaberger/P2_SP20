
#Turtle Recursion (30pts)

#1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)
import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_screen = turtle.Screen()

my_screen.bgcolor('pink')

my_turtle.speed(2000)
def recursive_h(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(height * 2)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height * 2)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(180)
        my_turtle.forward(height * 2)
        recursive_h(x + height, y + height, height / 2, depth - 1)
        recursive_h(x - height, y + height, height / 2, depth - 1)
        recursive_h(x - height, y - height, height / 2, depth - 1)
        recursive_h(x + height, y - height, height / 2, depth - 1)

recursive_h(0, 0, 150, 5)

my_screen.delay(10)
my_screen.clear()

#2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)
# a geometric rose!
my_screen.bgcolor('light blue')
my_turtle.color('dark red')
my_turtle.speed(2000)

def recursive_h(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(90)
        my_turtle.forward(height)
        my_turtle.left(45)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(180)
        my_turtle.forward(height)
        my_turtle.left(247.5)
        my_turtle.forward(height)
        my_turtle.right(180)
        my_turtle.forward(height)
        my_turtle.left(135)
        my_turtle.forward(height)
        my_turtle.left(180)
        my_turtle.forward(height)
        my_turtle.right(157.5)
        recursive_h(x + height * .3826834, y + height + height * .923879, height / 2, depth - 1)
        recursive_h(x + -height *.3826834, y + height + height * .923879, height / 2, depth - 1)
        recursive_h(x + height / (2 ** .5), y + height + (height / (2 ** .5)), height / 2, depth - 1)
        recursive_h(x + -height / (2 ** .5), y + height + (height / (2 ** .5)), height / 2, depth - 1)



recursive_h(0, 330, 150, 5)

my_screen.clear()

#3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)
my_screen.bgcolor('light green')
my_turtle.color('black')
my_turtle.speed(2000)

def recursive_h(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.width(2)
        my_turtle.fillcolor('light blue')
        my_turtle.begin_fill()
        my_turtle.setheading(0)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.end_fill()
        recursive_h(x - height / 2, y - height / 2, height / 2, depth - 1)
        recursive_h(x - height / 2, y + height, height / 2, depth - 1)
        recursive_h(x + height, y + height, height / 2, depth - 1)
        recursive_h(x + height, y - height / 2, height / 2, depth - 1)


recursive_h(-100, -150, 200, 4)


my_screen.exitonclick()
 #Each fractal should
 #- be recursive
 #- have a depth of at least 4
 #- be contained on the screen
 #swap 2 and 3

  #Have fun!

