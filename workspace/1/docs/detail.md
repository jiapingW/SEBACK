## Class description: The function of each class and its member attributes and member functions need to explain its function and meaning.

### Snake Class
The `Snake` class represents the snake in the game. It has the following member attributes:

- `position` (Tuple[int, int]): The current position of the snake on the grid.
- `direction` (Tuple[int, int]): The current direction of the snake's movement.
- `body` (List[Tuple[int, int]]): The positions of all the segments of the snake's body.

The `Snake` class has the following member functions:

- `move(self) -> None`: Updates the position of the snake based on its current direction of movement.
- `grow(self) -> None`: Adds a new segment to the snake's body, making it longer.
- `collides_with(self, position: Tuple[int, int]) -> bool`: Checks if the snake's head collides with a given position on the grid.

### Food Class
The `Food` class represents the food in the game. It has the following member attributes:

- `position` (Tuple[int, int]): The current position of the food on the grid.

The `Food` class has the following member functions:

- `generate_position(self, grid_size: Tuple[int, int]) -> Tuple[int, int]`: Generates a random position for the food on the grid.

### Game Class
The `Game` class represents the game state. It has the following member attributes:

- `grid_size` (Tuple[int, int]): The size of the grid.
- `score` (int): The current score of the game.
- `snake` (Snake): The snake object.
- `food` (Food): The food object.
- `game_over` (bool): A flag indicating whether the game is over or not.

The `Game` class has the following member functions:

- `update(self) -> None`: Updates the game state by moving the snake, checking for collisions, and updating the score.
- `handle_input(self, key: int) -> None`: Handles user input and updates the snake's direction accordingly.
- `display(self) -> None`: Displays the current game state on the command line interface.

### CLI Class
The `CLI` class represents the command line interface for the game. It has the following member attributes:

- `game` (Game): The game object.

The `CLI` class has the following member functions:

- `run(self) -> None`: Runs the game loop and handles user input.
