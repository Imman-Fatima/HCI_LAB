import turtle
# Create screen
screen = turtle.Screen()
screen.title("Circle as a Button")
screen.bgcolor("white")
# Create turtle
button = turtle.Turtle()
button.speed(0)
button.hideturtle()
# Function to draw circle button
def draw_button(color, label):

    button.clear()
    button.penup()
    button.goto(0, -50)
    button.pendown()

    button.color(color)
    button.begin_fill()
    button.circle(50)
    button.end_fill()

    # Write label inside circle
    button.penup()
    button.goto(0, -10)
    button.color("white")
    button.write(label, align="center",
                 font=("Arial", 12, "bold"))

# Draw initial button
draw_button("blue", "Click Me")

# Function for mouse click
def click_button(x, y):

    # Check if click is inside circle
    if x*x + y*y <= 50*50:

        # Change button colour and text
        draw_button("green", "Clicked!")

    else:
        print("Click outside the button!")

# Detect mouse click
screen.onclick(click_button)

# Keep window open
turtle.done()
