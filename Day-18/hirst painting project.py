# import colorgram
import random
import turtle as t

# ------------------------------
# Extract colors from an image
# (Run this section once to generate the RGB color list,
# then comment it out after copying the output.)
# ------------------------------

# colours = colorgram.extract("Day-18/images.jpg", 30)
# rgb_colours = []
#
# for colors in colours:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     rgb = (r, g, b)
#     rgb_colours.append(rgb)
#
# print(rgb_colours)

# List of RGB colors extracted from the image
colour_list = [
    (180, 176, 8), (177, 5, 60), (9, 141, 33), (241, 69, 7),
    (234, 13, 134), (42, 195, 236), (241, 23, 150), (87, 4, 92),
    (8, 131, 206), (233, 161, 48), (194, 6, 3), (247, 67, 13),
    (243, 225, 48), (10, 167, 131), (252, 229, 0), (209, 129, 176),
    (253, 3, 6), (115, 187, 153), (242, 158, 205), (252, 7, 4),
    (33, 180, 215), (150, 218, 184), (243, 168, 157), (141, 212, 228),
    (9, 118, 3), (111, 10, 7)
]

# Create a Turtle object that will draw the dots
dots = t.Turtle()

# Create the drawing screen
screen = t.Screen()

# Allow Turtle to use RGB color values (0–255)
t.colormode(255)

# Set the drawing speed to the fastest
dots.speed("fastest")

# Lift the pen so movement doesn't draw lines
dots.penup()

# Hide the turtle cursor for a cleaner drawing
dots.hideturtle()

# Move the turtle to the bottom-left starting position
dots.setheading(225)   # Face southwest
dots.forward(300)      # Move to starting point
dots.left(200)         # Adjust direction (optional)
dots.setheading(0)     # Face east

# Total number of dots to draw (10 × 10 grid)
number_of_dots = 100

# Draw the grid of colored dots
for dot_count in range(1, number_of_dots + 1):

    # Draw a dot with a random color from the list
    dots.dot(20, random.choice(colour_list))

    # Move forward to the next dot position
    dots.forward(50)

    # After every 10 dots, move to the beginning of the next row
    if dot_count % 10 == 0:
        dots.setheading(90)    # Face north
        dots.forward(50)       # Move up one row
        dots.setheading(180)   # Face west
        dots.forward(500)      # Return to the first column
        dots.setheading(0)     # Face east to start the next row

# Keep the window open until it is clicked
screen.exitonclick()