
import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.title("2D Geometric Transformations")
screen.setup(900, 750)
screen.bgcolor("#F5F7FA")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.hideturtle()

# Draw coordinate axes
def draw_axes():
    t.penup()
    t.goto(-350, 0)
    t.pendown()
    t.color("gray")
    t.goto(350, 0)

    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.goto(0, 300)

    t.penup()
    t.goto(0, 0)
    t.dot(8, "black")

# Function to draw square
def draw_square(points, color):

    t.penup()
    t.goto(points[0])
    t.color(color)
    t.pendown()

    for point in points[1:]:
        t.goto(point)

    t.goto(points[0])
    t.penup()

# Function to write labels
def write_label(x, y, message, color):

    t.penup()
    t.goto(x, y)
    t.color(color)
    t.write(message, font=("Arial", 11, "bold"))

# Coordinate axes
draw_axes()

# Original square - BLACK
original = [
    (0, 0),
    (60, 0),
    (60, 60),
    (0, 60)
]

draw_square(original, "black")
write_label(5, -25, "Original", "black")

# Translation - BLUE
translated = []

for x, y in original:
    translated.append((x + 120, y + 60))

draw_square(translated, "blue")
write_label(125, 125, "Translation", "blue")

# Scaling - RED
scaled = []

for x, y in original:
    scaled.append((x * 2, y * 2))

draw_square(scaled, "red")
write_label(5, 135, "Scaling 2x", "red")

# Rotation - GREEN
def rotate_square(angle):

    rotated = []
    rad = math.radians(angle)

    for x, y in original:

        new_x = x * math.cos(rad) - y * math.sin(rad)
        new_y = x * math.sin(rad) + y * math.cos(rad)

        rotated.append((new_x, new_y))

    draw_square(rotated, "green")

# Three rotated copies
rotate_square(30)
rotate_square(60)
rotate_square(90)

write_label(-190, 115, "Rotation: 30, 60, 90", "green")

# Main heading
t.penup()
t.goto(-150, 310)
t.color("black")
t.write("2D TRANSFORMATIONS",
        font=("Arial", 20, "bold"))

# Finish
turtle.done()
