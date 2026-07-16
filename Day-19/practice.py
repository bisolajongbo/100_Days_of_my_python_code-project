from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

# To move forward
def move_forwards():
    tim.forward(10)
# To move backward
def move_backwards():
    tim.backward(10)
    # To move counter_clockwise
def counter_clockwise():
#    new= tim.heading()+10
#    tim.setheading(new)
        tim.left(10)

  # To move clockwise
def clockwise():

  tim.right(10)
#   new= tim.heading()+10
# # tim.setheading(new)

# To move clear drawing
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear_drawing)
screen.exitonclick()