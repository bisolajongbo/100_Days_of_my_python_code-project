# Day-23: TURTLE CROSSING GAME
## Project Overview
This project is a Turtle Crossing game where the player controls a turtle attempting to safely cross a road with continuously moving cars. The game ends with a **"Game Over"** message if the turtle collides with a car. Each time the turtle successfully reaches the other side, the player advances to the next level, and the cars increase in speed, making the game progressively more difficult. This project was developed by applying the Python programming concepts and skills I have learned.


## What I Learnt
* Learned how to structure the game using multiple classes (**Scoreboard**, **Player**, and **CarManager**) to improve code organization, reusability, and maintainability.

* Applied **inheritance** in the **Scoreboard** and **Player** classes to extend the `Turtle` class with custom attributes and behaviors.

* Implemented keyboard event handling with `screen.onkey()` to enable responsive turtle movement based on user input.

* Managed the game's execution using a continuous game loop with `time.sleep()` to control the update rate and create smooth gameplay.

* Used the Turtle graphics module to display dynamic on-screen information, including the current level and the **"Game Over"** message.

* Controlled the game's progression by updating variables that increase the speed of the cars after each successful level, making the game more challenging.

## How It Works
**main.py:**
This is the main file that manages the overall game logic. It initializes the game window, creates the key game objects (the player, cars, and scoreboard), and sets up keyboard controls for player movement. It also runs the main game loop, where cars are generated at random, continuously move across the screen, the player advances to the next level after reaching the finish line, and the game ends if the player collides with a car.

**player.py:**
This module contains the `Player` class, which inherits from `turtle.Turtle`. It defines the player's appearance, starting position, and orientation. It also includes methods for moving the turtle forward and backward, along with a reset method that returns the player to the starting position after successfully crossing the road.

**car_manager.py:**
This module is responsible for creating and managing the cars. The `CarManager` class generates cars with random colors and positions, stores them in a list, and moves them across the screen. As the player progresses through the levels, the cars increase in speed. It also detects collisions between the player and the cars, returning `True` when a collision occurs so the game can end.

**scoreboard.py:**
This module manages the game's scoring and display elements. It draws the finish line, shows the player's current level, updates the level after each successful crossing, and displays a **"GAME OVER"** message when the player is hit by a car.


