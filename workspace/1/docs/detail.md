## Class description: The function of each class and its member attributes and member functions need to explain its function and meaning.

### Game class:
The `Game` class represents the snake game. It has the following member attributes:
- `score` (int): Represents the player's score.

And the following member functions:
- `start(self) -> None`: Starts the game by initializing the snake, food, and game screen. It also starts the game loop.
- `end(self) -> None`: Ends the game by displaying the game over screen and updating the high score leaderboard if necessary.
- `pause(self) -> None`: Pauses the game by stopping the game loop and displaying a pause screen.
- `resume(self) -> None`: Resumes the game by restarting the game loop.

### Snake class:
The `Snake` class represents the snake in the game. It has the following member attributes:
- `direction` (int): Represents the current direction of the snake's movement.
- `body` (List[Tuple[int, int]]): Represents the positions of the snake's body segments.

And the following member functions:
- `move(self) -> None`: Moves the snake in the current direction by updating the positions of its body segments.
- `change_direction(self, direction: int) -> None`: Changes the direction of the snake's movement.
  - `direction` (int): The new direction of the snake's movement.
- `eat_food(self) -> None`: Increases the snake's length by adding a new body segment at the head.
- `collide_with_wall(self) -> bool`: Checks if the snake has collided with the game screen's boundaries.
- `collide_with_self(self) -> bool`: Checks if the snake has collided with its own body.

### Food class:
The `Food` class represents the food in the game. It has the following member attributes:
- `position` (Tuple[int, int]): Represents the position of the food on the game screen.

And the following member functions:
- `generate(self) -> None`: Generates a new position for the food randomly on the game screen.

### GameScreen class:
The `GameScreen` class represents the game screen. It has the following member attributes:
- `width` (int): Represents the width of the game screen.
- `height` (int): Represents the height of the game screen.

And the following member functions:
- `draw_snake(self, snake: Snake) -> None`: Draws the snake on the game screen.
  - `snake` (Snake): The snake object to be drawn.
- `draw_food(self, food: Food) -> None`: Draws the food on the game screen.
  - `food` (Food): The food object to be drawn.
- `draw_score(self, score: int) -> None`: Draws the player's score on the game screen.
  - `score` (int): The player's score.
- `draw_game_over(self) -> None`: Draws the game over screen on the game screen.