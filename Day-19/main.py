from turtle import Turtle, Screen
import random

# Variable to control whether the race is running
is_race_on = False

# Create the screen object
screen = Screen()
screen.listen()

# Set the screen size
screen.setup(width=500, height=400)

# Set the screen background color
screen.bgcolor("black")

# Set the game title
screen.title("Turtle race")

# Ask the user to bet on which turtle will win
user_bet = screen.textinput(
    title="Make a bet",
    prompt="Who will win this race? Enter a colour: "
)

# List of turtle colours
colors = ["red", "blue", "green", "orange", "yellow", "white"]

# Starting y-coordinates for each turtle
y_position = [-70, -40, -10, 20, 50, 80]

# Store all turtle objects
all_turtle = []

# Create six turtles with different colours and starting positions
for turtle_index in range(0, 6):
    t_game = Turtle(shape="turtle")
    t_game.penup()  # Prevent drawing lines while moving to the start
    t_game.goto(x=-230, y=y_position[turtle_index])  # Starting position
    t_game.color(colors[turtle_index])  # Assign a unique colour
    all_turtle.append(t_game)  # Add turtle to the list

# Start the race only if the user entered a bet
if user_bet:
    is_race_on = True

    # Keep the race running until a turtle reaches the finish line
    while is_race_on:

        # Move each turtle one after another
        for turtle in all_turtle:

            # Check if the turtle has crossed the finish line
            if turtle.xcor() > 230:

                # Stop the race
                is_race_on = False

                # Get the winning turtle's colour
                winning_color = turtle.pencolor()

                # Check if the user's bet matches the winning turtle
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner")

            # Generate a random distance for the turtle to move
            random_distance = random.randint(0, 10)

            # Move the turtle forward by the random distance
            turtle.forward(random_distance)

# Keep the window open until the user clicks on it
screen.exitonclick()