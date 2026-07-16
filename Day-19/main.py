from turtle import Turtle,Screen
import random
is_race_on = False
screen=Screen()
screen.listen()
screen.setup(width=500,height=400)# Screen is width is 500 and height is 400
user_bet = screen.textinput(title="Make a bet",prompt="Who will win this race bet? Enter colour: ")
colors = ["red","blue","green","orange","yellow","brown"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []

for  turtle_index in range(0,6):
 t_game=Turtle(shape = "turtle")
 t_game.penup()
 t_game.goto(x=-230,y= y_position[turtle_index])
 t_game.color(colors[turtle_index])
 all_turtle.append(t_game)

if user_bet:
 is_race_on = True

 while is_race_on:
     
     
     for turtle in all_turtle:
        if turtle.xcor() > 230:
          
          is_race_on = False

          winning_color = turtle.pencolor()

          if  winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner")
          else:
             print(f"You've lost! The {winning_color} turtle is the winner")
          


        random_distance=random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()