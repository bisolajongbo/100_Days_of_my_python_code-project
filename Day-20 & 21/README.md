# Day-20 & 21: Snake Game
## Project Overview
This project is a classic Snake Game built with Python's Turtle Graphics module. The player controls a snake that moves around the screen, eats randomly generated food to increase its length and score, and avoids colliding with the walls or its own tail. The game ends immediately when the snake hits a wall or itself.The project is built using Python's Turtle graphics module and demonstrates Object-Oriented Programming (OOP) principles such as classes and inheritance. It also incorporates global variables, list slicing, event handling, and core game logic to create an interactive Snake game.

### What I Learnt

* Creating and managing multiple objects using Object-Oriented Programming (OOP).
* Applying inheritance to extend the functionality of the `Turtle` class when building the **Food** and **Scoreboard** classes.
* Using list slicing (`snake.segments[1:]`) to efficiently check for self-collisions by comparing the snake's head with the rest of its body.
* Implementing keyboard event listeners to control the snake's movement through key bindings.
* Effectively using global variables and loops to manage the game flow and state.
* Organizing a Python project into multiple files and modules to improve code readability, maintainability, and reusability.


## How It Works
### **main.py**

This is the main entry point of the game. It initializes the game window, creates the snake, food, and scoreboard objects, and manages the main game loop.

* Methods such as `screen.setup()`, `screen.bgcolor()`, and `screen.title()` are used to configure the game window, including its size, background color, and title.
* Keyboard event listeners are registered using `screen.onkey()` to allow the player to control the snake with the arrow keys.
* The game loop continuously updates the screen, moves the snake, and checks for collisions with food, the walls, and the snake's own body.
* When a collision with a wall or the snake's tail occurs, the game ends and a **Game Over** message is displayed.

### **snake.py**

This module contains the `Snake` class, which manages the snake's creation, movement, growth, and direction.

* The `create_snake()` and `add_segment()` methods initialize the snake by creating multiple body segments and storing them in a list.
* The `move()` method updates each segment's position so that it follows the segment in front of it, creating smooth snake movement.
* The `up()`, `down()`, `left()`, and `right()` methods change the snake's direction while preventing it from reversing into itself.
* The `extend()` method adds a new segment to the end of the snake whenever food is eaten, increasing its length.

### **food.py**

This module defines the `Food` class, which inherits from the `Turtle` class and represents the food the snake consumes.

* The class customizes the food's appearance by setting its shape, size, color, and speed.
* The `refresh()` method generates a new random position for the food each time the snake eats it, ensuring continuous gameplay.

### **scoreboard.py**

This module manages the game's scoring system and displays messages on the screen.

* The `update_scoreboard()` method displays the current score at the top of the game window.
* The `increase_score()` method increments the score, clears the previous score, and updates the display whenever the snake eats food.
* The `Game_over()` method displays a **"GAME OVER"** message at the center of the screen when the game ends.


   ## Output
 <video controls src="Snake game.mp4" title="Title"></video>

 
