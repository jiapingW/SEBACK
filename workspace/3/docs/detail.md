## Class Description: Snake
The `Snake` class represents the snake object in the game. It has the following member attributes:

- `x` (int): The x-coordinate of the snake's head position.
- `y` (int): The y-coordinate of the snake's head position.
- `dx` (int): The change in x-coordinate for the snake's movement direction.
- `dy` (int): The change in y-coordinate for the snake's movement direction.
- `body` (List[Tuple[int, int]]): A list of tuples representing the coordinates of the snake's body segments.

The `Snake` class has the following member functions:

- `move() -> None`: Updates the snake's position based on the current movement direction.
- `grow() -> None`: Adds a new body segment to the snake's body.
- `collides_with_food(food: Food) -> bool`: Checks if the snake's head position overlaps with the food's position.
  - Parameters:
    - `food` (Food): The food object to check collision with.
  - Returns:
    - `bool`: True if the snake's head position overlaps with the food's position, False otherwise.
- `collides_with_self() -> bool`: Checks if the snake's head position overlaps with any part of its body.
  - Returns:
    - `bool`: True if the snake's head position overlaps with any part of its body, False otherwise.
- `collides_with_boundary(width: int, height: int) -> bool`: Checks if the snake's head position is outside the boundaries of the grid.
  - Parameters:
    - `width` (int): The width of the grid.
    - `height` (int): The height of the grid.
  - Returns:
    - `bool`: True if the snake's head position is outside the boundaries of the grid, False otherwise.
- `draw(surface: pygame.Surface, cell_size: int) -> None`: Draws the snake on the given surface using a specific character.
  - Parameters:
    - `surface` (pygame.Surface): The surface to draw the snake on.
    - `cell_size` (int): The size of each cell in the grid.

## Class Description: Food
The `Food` class represents the food object in the game. It has the following member attributes:

- `x` (int): The x-coordinate of the food's position.
- `y` (int): The y-coordinate of the food's position.

The `Food` class has the following member functions:

- `draw(surface: pygame.Surface, cell_size: int) -> None`: Draws the food on the given surface using a specific character.
  - Parameters:
    - `surface` (pygame.Surface): The surface to draw the food on.
    - `cell_size` (int): The size of each cell in the grid.

## Class Description: Game
The `Game` class represents the main game object. It has the following member attributes:

- `width` (int): The width of the grid.
- `height` (int): The height of the grid.
- `surface` (pygame.Surface): The surface to display the game on.
- `snake` (Snake): The snake object in the game.
- `food` (Food): The food object in the game.
- `score` (int): The number of food items eaten by the snake.

The `Game` class has the following member functions:

- `__init__(width: int, height: int) -> None`: Initializes a new game with the specified width and height.
  - Parameters:
    - `width` (int): The width of the grid.
    - `height` (int): The height of the grid.
- `update() -> None`: Updates the game state.
- `handle_input() -> None`: Handles user input.
- `draw() -> None`: Draws the game on the surface.
- `run() -> None`: Runs the game loop.

## Class Description: CLI
The `CLI` class represents the command line interface for the game. It has the following member attributes:

- `game` (Game): The game object.

The `CLI` class has the following member functions:

- `__init__(game: Game) -> None`: Initializes a new CLI with the specified game.
  - Parameters:
    - `game` (Game): The game object.
- `run() -> None`: Runs the game in the command line interface.