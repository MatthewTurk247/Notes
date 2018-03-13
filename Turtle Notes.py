import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.shape('turtle')
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('pink')
my_turtle.fillcolor('white')
my_turtle.color('white')
my_turtle.width(5)

my_turtle.begin_fill() # starting a new object that we will fill in
# The size of the screen is 215 in each direction
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

my_turtle.fillcolor('blue')
my_turtle.color('blue')

my_turtle.up() # picking the pencil up
my_turtle.goto(200, 200)
my_turtle.down() # put pencil back down
my_turtle.begin_fill()
my_turtle.goto(250, 250)
my_turtle.goto(250, 200)
my_turtle.goto(200, 250)
my_turtle.end_fill()

my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()

# move with headings
my_turtle.fillcolor('red')
my_turtle.color('red')
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)

# Recursive rectangle pattern
# library
my_screen.clear()
# robotics, raspberry pi

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width, height)
        my_turtle.down()
        my_turtle.goto(width, -height)
        my_turtle.goto(-width, -height)
        my_turtle.goto(-width, height)
        my_turtle.goto(width, height)
        recursive_rect(1.5*width, 1.5*height, depth - 1)

recursive_rect(20, 20, 10)

my_screen.clear()
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.color('black')
my_turtle.width(1)

def recursive_bracket(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size/2)
        my_turtle.goto(x + size, y - size/2)
        recursive_bracket(x + size, y + size/2, size/2, depth - 1)
        recursive_bracket(x + size, y - size/2, size/2, depth - 1)

recursive_bracket(-300, 0, 300, 7)

my_screen.exitonclick()