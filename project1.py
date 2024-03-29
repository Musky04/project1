import turtle

# Function to draw a cloud using a series of overlapping circles
def draw_cloud(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")  # Set the fill color to white for the cloud
    turtle.begin_fill()
    # Draw several circles to form a cloud shape
    turtle.circle(20)
    turtle.penup()
    turtle.goto(x + 20, y + 20)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(x + 40, y)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(x + 60, y + 20)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.goto(x + 80, y)
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()

wn = turtle.Screen()
wn.bgcolor("green") 

pen = turtle.Turtle()
pen.speed()

# Draw the sky
pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("deepskyblue")  # Set the pen color
pen.begin_fill()
for i in range(2):
    pen.forward(800)
    pen.left(90)
    pen.forward(500)
    pen.left(90)
pen.end_fill()

# Draw the sun
pen.penup()
pen.goto(-320, 225)
pen.pendown()
pen.color("yellow")  # Set the pen and fill color to yellow
pen.begin_fill()
pen.circle(35)
pen.end_fill()

# Draw the clouds
draw_cloud(pen, 100, 200)
draw_cloud(pen, -50, 250)
draw_cloud(pen, -200, 220)

# Draw a blue square (house)
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.color("blue")  # Set the pen color to blue
pen.fillcolor("blue")  # Set the fill color to blue
pen.begin_fill()
for i in range(4):
    pen.forward(170)
    pen.left(90)
pen.end_fill()

# Draw a dark blue rectangle (door)
pen.penup()
pen.goto(20, 130)
pen.pendown()
pen.color("darkblue")  # Set the pen and fill color to darkblue
pen.begin_fill()
for i in range(2):
    pen.forward(40)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Draw a triangle (roof)
pen.penup()
pen.goto(-127, 70)
pen.pendown()
pen.fillcolor("darkblue")  # Set the fill color to darkblue
pen.begin_fill()
for i in range(3):
    pen.forward(225)
    pen.left(120)
pen.end_fill()

# Draw windows
windows = [(0, 0), (-80, 0)]
for (x, y) in windows:
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("blue", "deepskyblue")
    pen.begin_fill()
    for i in range(4):
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    # Draw the window panes
    pen.penup()
    pen.goto(x, y + 25)
    pen.pendown()
    pen.color("black")
    pen.forward(50)

    pen.penup()
    pen.goto(x + 25, y)
    pen.pendown()
    pen.left(90)  # Rotate the pen to draw vertical line
    pen.forward(50)
    pen.right(90)  # Reset the pen rotation

# Draw a grey rectangle (path)
pen.penup()
pen.goto(-40, -97)
pen.pendown()
pen.color("grey")  # Set the pen and fill color to grey
pen.begin_fill()
for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()

# Draw a black circle (doorknob)
pen.penup()
pen.goto(-30, -60)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()


wn.exitonclick()



