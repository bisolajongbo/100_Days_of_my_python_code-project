import turtle as t
import random

# Create a Turtle object that will draw the spirograph
spirograph = t.Turtle()

# Enable RGB color mode (0–255)
t.colormode(255)

# Function to generate a random RGB color
def random_color():
    # Generate random values for red, green, and blue
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Store the RGB values as a tuple
    color = (r, g, b)

    # Return the randomly generated color
    return color

# Create the drawing window
screen = t.Screen()

# Set the turtle's drawing speed to the fastest
spirograph.speed("fastest")

# Function to draw a spirograph pattern
def draw_spirograph(size_of_circle):

    # Repeat until a full 360° rotation is completed
    for _ in range(int(360 / size_of_circle)):

        # Change the pen color to a random RGB color
        spirograph.color(random_color())

        # Draw a circle with a radius of 100
        spirograph.circle(100)

        # Rotate the turtle by the specified angle
        spirograph.setheading(spirograph.heading() + size_of_circle)

# Draw the spirograph using a 5-degree rotation
draw_spirograph(5)

# Keep the graphics window open until it is clicked
screen.exitonclick()