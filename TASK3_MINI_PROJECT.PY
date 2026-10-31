import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Solar System Animation")
screen.bgcolor("#050816")
screen.tracer(0)

# Drawing turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Orbit settings
center_x = 0
center_y = 0

# Planets: name, orbit radius, planet size, color, speed
planets = [
    ("Mercury", 75, 5, "#B7B7B7", 4.0),
    ("Venus", 115, 8, "#E6B566", 2.5),
    ("Earth", 165, 10, "#3498DB", 1.8),
    ("Mars", 215, 7, "#E76F51", 1.4),
    ("Jupiter", 280, 18, "#D4A373", 0.9),
    ("Saturn", 350, 15, "#E9C46A", 0.6)
]

# Draw a circle
def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw orbit paths
def draw_orbits():
    for name, orbit, size, color, speed in planets:
        pen.penup()
        pen.goto(0, -orbit)
        pen.pensize(1)
        pen.color("#35415F")
        pen.pendown()
        pen.circle(orbit)

# Draw Sun
def draw_sun():
    draw_circle(0, 0, 35, "#FDB813")
    draw_circle(0, 0, 28, "#FFDD55")

# Draw planet labels
def draw_label(x, y, name):
    pen.penup()
    pen.goto(x + 12, y + 10)
    pen.color("white")
    pen.write(name, font=("Arial", 8, "normal"))

# Draw Saturn's ring
def draw_saturn_ring(x, y):
    pen.penup()
    pen.goto(x - 23, y - 4)
    pen.color("#F4D58D")
    pen.pensize(3)
    pen.pendown()
    pen.goto(x + 23, y + 4)

# Animation angles
angles = [0, 0, 0, 0, 0, 0]
moon_angle = 0

# Animation loop
while True:
    pen.clear()

    # Draw stars
    for x, y in [
        (-430, 300), (-300, 250), (-180, 330),
        (200, 300), (400, 200), (350, -250),
        (-400, -200), (150, -300), (-100, -250)
    ]:
        draw_circle(x, y, 2, "white")

    # Draw orbits and Sun
    draw_orbits()
    draw_sun()

    # Sun label
    pen.penup()
    pen.goto(-20, -55)
    pen.color("white")
    pen.write("SUN", font=("Arial", 10, "bold"))

    # Draw planets
    for i, planet in enumerate(planets):
        name, orbit, size, color, speed = planet

        angle = math.radians(angles[i])

        x = orbit * math.cos(angle)
        y = orbit * math.sin(angle)

        draw_circle(x, y, size, color)
        draw_label(x, y, name)

        # Saturn ring
        if name == "Saturn":
            draw_saturn_ring(x, y)

        # Moon orbiting Earth
        if name == "Earth":
            moon_angle += 4
            moon_rad = math.radians(moon_angle)

            moon_x = x + 18 * math.cos(moon_rad)
            moon_y = y + 18 * math.sin(moon_rad)

            draw_circle(moon_x, moon_y, 3, "#DDDDDD")

        angles[i] += speed

    # Project heading
    pen.penup()
    pen.goto(0, 350)
    pen.color("#F1FAEE")
    pen.write(
        "SOLAR SYSTEM ANIMATION",
        align="center",
        font=("Arial", 22, "bold")
    )

    screen.update()
    time.sleep(0.03)

