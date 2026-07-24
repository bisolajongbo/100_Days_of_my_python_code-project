# Day-22: PONG GAME 
## Project Overview
This is a classic Pong game developed using Python's Turtle graphics module. The game features two paddles and a ball, where each player controls a paddle to keep the ball in play. If a player fails to return the ball, their opponent earns a point. The match continues until one player reaches 5 points and is declared the winner.

While building this project, I applied Object-Oriented Programming (OOP) principles, including inheritance, and implemented key game development concepts such as game loops, keyboard event handling, collision detection, and real-time screen updates using `Turtle.Screen()`.


## What I Learnt
* Applied Object-Oriented Programming (OOP) principles to divide the game into reusable and maintainable components, making the code easier to update and extend.

* Developed separate classes such as **Paddle**, **Ball**, **Score**, and **Border** by inheriting from the `Turtle` class, allowing each class to implement its own game-specific functionality.

* Enabled responsive player controls by capturing keyboard input with the `listen()` and `onkey()` methods, allowing the paddles to move in real time.

* Improved code organization and readability by separating the game's functionality into dedicated modules: `main.py`, `ball.py`, `paddle.py`, `score.py`, and `border.py`.

## How It Works
**main.py:** Acts as the main driver of the game by setting up the game window, creating all game objects (paddles, ball, scoreboard, and border), configuring keyboard controls, running the main game loop, handling collision detection, adjusting the ball's speed, and determining when a player wins the game.

**paddle.py:** Defines the `Paddle` class by inheriting from the `Turtle` class. It creates the left and right paddles and provides methods for moving them up and down while ensuring they remain within the game boundaries.

**ball.py:** Implements the `Ball` class, which controls the ball's movement, detects collisions with walls and paddles, changes its direction when collisions occur, gradually increases its speed after each paddle hit, and introduces slight random angle variations to make gameplay more dynamic.

**score.py:** Contains the `Score` class, responsible for tracking both players' scores, updating the scoreboard in real time, and displaying the winning message once a player reaches 5 points.

**line.py:** Creates the visual boundaries of the game by drawing the center dividing line and the top border, giving the Pong arena a clear and organized layout.


   

   
   

 
