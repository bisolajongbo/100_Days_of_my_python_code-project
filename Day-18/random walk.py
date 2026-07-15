import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
random_walk = t.Turtle()
# screen=t.Screen()
# screen.exitonclick
direction =[0,90,180,270]#This direction are in angles
random_walk.pensize(5)
random_walk.speed("normal")
for _ in range(200):
    random_walk.forward(30)
    random_walk.color(random.choice(colours))
    random_walk.setheading(random.choice(direction))
    



