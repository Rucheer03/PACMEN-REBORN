
#  🕹️ **PACMAN-REBORN** 


## Group Members:

- **Rucheer patel - 202404034**
- **Preet patel - 202404027**





## Introduction
 
 We have inspect pacman game for END-SEM project.
In which pacman is our protagonist, score is increased as food is eaten by pacman but ghosts are there to resist him.If ghost and pacman collide with each other game ends.



## 🎯 Why This Project?
   
   - This game have more complex features than previous Projects.like 3 enemies which make game more difficult and  walls which bound pacman to escape from ghost And  there are other severe features like colours and sound effect

  

## Requirements


### Platform

- **macOS and windows**.

### Compiler

- A python compiler that supports the **python 3.6**  or later:
 ### libraries

 - **pygame**

  **install with**:
    
   ``` bash
    pip install pygame
```

## 🚀 How to Run the Game

  1. **Open** your terminal or command prompt.  
2. **Navigate** to the folder where the game file exists:
  3. Run the game with,
  ```bash
  python main.py
  ```

  ## Key Controls

- **Arrow Keys** for controlling the pacman:
  - **Up Arrow**: move the pacman up.
  - **Left Arrow**: Move the pacman left.
  - **Right Arrow**: Move the pacman right.
  - **Down Arrow**: Move the pacman down.
  



  

# Screenshots

![img alt](https://github.com/Rucheer03/PACMEN-REBORN/blob/main/screenshot.jpeg)



# Game Flow Explanation

## Starting the Game  
When you open the game, it sets up a window with a maze full of paths and walls. The main Pac-Man appears at a starting point, and enemies ghosts(enemies) are placed in other parts of the maze. Small dots are scattered along the paths for the Pac-Man to collect.

## Gameplay Loop  
The game runs in a continuous loop, updating everything 30 times per second to keep it smooth. Here’s what happens in each loop:

## Check for Input  
- The game looks for keyboard presses.  
- **Arrow keys** move the character left, right, up, or down.  
- **Escape key** pauses or quits the game.  

## Move Characters  
- The player’s character moves based on the arrow keys.  
- If it tries to go into a wall, the game stops it.  
- Enemies move on their own, patrolling the maze and changing direction when they hit walls.  

## Check Collisions  
- If the player touches a dot:  
  - The dot disappears.  
  - The score increases.  
- If the player touches an enemy:  
  - The game shows an explosion.  
  - The game ends.  

## Update the Screen  
The game redraws everything:  
- The maze walls and paths.  
- Remaining dots.  
- The player and enemies in their new positions.  
- The current score.  

## Menus and Options  
At the start, a menu lets you choose:  
- **Start**: Begins a new game.  
- **About**: Shows game instructions.  
- **Exit**: Closes the game.  

Use the **arrow keys** to navigate and **Enter** to select options. During gameplay, pressing **Escape** returns to the menu. 

--- 

## Visuals and Effects  


- The player’s mouth opens and closes as it moves, creating a chewing animation.  
- Enemies glide smoothly through the maze.  
- An explosion animation plays if the player loses.  

---
## Ending the Game  
- If you lose or choose **Exit**:  
  - The window closes.  
  - The program stops.  

---
# Data Structures used in Pacman Game(file wise)
## 1. `main.py`

This is the core game loop file, handling initialization, rendering, input, and game state.

### Data Structures Used:

* **`list`**:
    * Maze grid (loaded from `game.py` as a 2D list).
    * List of collectible item positions (`tuple`s).
    * List of enemy instances.
* **`pygame.Rect`**:
    * Player and enemy hitboxes.
    * Used for detecting wall and collectible collisions.
* **`bool`**:
    * Game state tracking (e.g., `running`, win/lose conditions).


### Where & How They're Used:

* `maze = load_maze('maze.txt')`: Loads a 2D `list` representing the maze layout (`#` = wall, `.` = collectible, space = empty path).
* `collectibles = get_collectibles(maze)`: Returns a `list` containing `tuple`s of `(x, y)` coordinates for each collectible found in the `maze` grid.
* Player and enemy positions are updated, and their `pygame.Rect` objects are used for collision detection against wall `Rect`s and collectible positions.

---
## 2. `player.py`

**Class: `Player`**

Encapsulates the player’s state and movement logic.

### Attributes & Their Data Types:

* **`x`, `y`** (`int`): Coordinates of the player.
* **`speed`** (`int`): Movement speed.
* **`direction`** (`str`): Current movement direction.
* **`next_direction`** (`str`): Direction queued by player input.
* **`rect`** (`pygame.Rect`): For collision detection and rendering.

### Functions:

* `__init__()`: Initializes player attributes (position, speed, etc.).
* `draw(screen)`: Draws the player character on the given screen surface using `pygame.draw`.
* `move(walls)`: Updates the player's `x`, `y` coordinates based on `speed` and `direction`. Uses the `list` of wall `Rect`s passed in `walls` for collision checks.
* `update_direction(keys)`: Reads keyboard input (`keys`) to set the `next_direction`.
* `check_collision(walls)`: Validates potential movement against the `list` of wall `Rect`s to prevent moving through walls.

### Data Structures Used:

* `pygame.Rect`: Represents the player's collision hitbox.
* `list` (of wall `pygame.Rect`s): Used by `move()` and `check_collision()` to validate movement paths.

---
## 3. `enemies.py`

**Class: `Enemy`**

Manages AI or random movement for ghosts/enemies.

### Attributes & Their Data Types:

* **`x`, `y`** (`int`): Coordinates of the enemy.
* **`speed`** (`int`): Movement speed.
* **`direction`** (`str`): Current movement direction.
* **`rect`** (`pygame.Rect`): Used for enemy collision detection.

### Functions:

* `__init__()`: Sets the enemy’s starting position and initial state.
* `draw(screen)`: Renders the enemy character on the screen surface.
* `move(walls)`: Moves the enemy based on its current logic (e.g., random, pathfinding) and handles collisions with the provided `list` of wall `Rect`s.
* `change_direction()`: Logic to pick a new direction, often triggered when hitting a wall or at an intersection.
* `check_collision(walls)`: Ensures enemies don’t move through walls by checking against the `list` of wall `Rect`s.

### Data Structures Used:

* `pygame.Rect`: Represents the enemy's collision hitbox.
* `list` (of wall `pygame.Rect`s): Used for collision detection to constrain enemy movement.

---
## 4. `game.py`


This file handles maze management (loading, parsing) and rendering.

### Functions & Data Structures:

* **`load_maze(filename)`**
    * **Returns**: A 2D `list` (list of lists) of characters (`#`, `.`, or space).
    * **How**: Reads the specified text file line by line. Each line becomes a row (a `list` of characters) in the main 2D `list`, effectively forming the game grid.
* **`draw_maze(screen, maze)`**
    * **Usage**: Iterates through the 2D `maze` grid (`list` of `list`s). For each cell containing a wall character (`#`), it draws a corresponding rectangle on the `screen`.
* **`get_collectibles(maze)`**
    * **Returns**: A `list` of `tuple`s.
    * **How**: Scans the 2D `maze` grid. Whenever it finds a collectible character (`.`), it calculates its `(x, y)` position in the game world and adds this `tuple` to the `list` which is then returned.

---
## Improvements and Features to be added
* We can add some special type of food such that after eating it ghost does not able to kill pacman for some period of time.
* A speed boost could temporarily make Pac-Man move faster, allowing quick escapes
* A ghost freeze could stop all ghost movement, giving the player a strategic advantage.

---
## Conclusion

The Pac-Man game remains one of the most iconic and influential arcade games of all time.  By controlling Pac-Man to navigate through mazes, avoid ghosts, and collect pellets, players experience a perfect blend of action and strategy. With the potential to introduce new features such as power-ups, modern graphics.  Overall, Pac-Man is a great example of how creative gameplay mechanics and engaging design can create a game that continues to entertain players for generations.

## License

This project is open source. Feel free to modify and distribute it as you like.
