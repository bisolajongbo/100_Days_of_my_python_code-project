from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

# Set the screen size
screen.setup(width=600, height=600)
# Set the background color
screen.bgcolor("black")
# Set the game title
screen.title("Bisola snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# Detect Collision with food
# using distance for turtle documentation
    if snake.head.distance(food) < 15:
        food.refresh()# calling refresh from food class
        snake.extend()
        score.increase_score()

# Detect Collision with wall
    if snake.head.xcor()>280  or  snake.head.xcor()<-280  or  snake.head.ycor()>280 or snake.head.ycor()<-280:
       game_is_on = False
       score.Game_over()

    # Detect collission with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.Game_over()
    # If head collide with any segment in the tail
    # trigger game_overl
    

    














































screen.exitonclick()