```python
class Game:
    def __init__(self, width: int, height: int):
        """
        Initializes a new game with the given width and height.
        Creates a new Snake and Food object.
        Initializes the score to 0.

        Attributes:
        width (int): The width of the game grid.
        height (int): The height of the game grid.
        score (int): The current score of the game.
        snake (Snake): The snake controlled by the player.
        food (Food): The food object in the game.
        """
        pass

    def start(self):
        """
        Starts the game. The snake starts moving based on the player's input.
        """
        pass

    def end(self):
        """
        Ends the game. Displays a game over message and the player's final score.
        """
        pass

    def restart(self):
        """
        Restarts the game. Resets the game state including the snake's length and position, score, and food position.
        """
        pass

    def update(self):
        """
        Updates the game state. Moves the snake, checks for collisions, generates food, and updates the score.
        """
        pass


class Snake:
    def __init__(self):
        """
        Initializes a new snake. The initial length of the snake is 1.

        Attributes:
        body (list): A list of coordinates representing the snake's body.
        direction (str): The current moving direction of the snake.
        """
        pass

    def move(self):
        """
        Moves the snake in the current direction. The snake moves one grid per input.
        """
        pass

    def grow(self):
        """
        Increases the length of the snake by 1. The new length is added at the end of the snake.
        """
        pass

    def collides_with_self(self) -> bool:
        """
        Checks if the snake collides with its own body.

        Returns:
        bool: True if the snake collides with its own body, False otherwise.
        """
        pass

    def collides_with_wall(self, width: int, height: int) -> bool:
        """
        Checks if the snake collides with the wall.

        Parameters:
        width (int): The width of the game grid.
        height (int): The height of the game grid.

        Returns:
        bool: True if the snake collides with the wall, False otherwise.
        """
        pass


class Food:
    def __init__(self):
        """
        Initializes a new food object.

        Attributes:
        position (tuple): The coordinates of the food on the game grid.
        """
        pass

    def generate(self, width: int, height: int, snake_body: list):
        """
        Generates a new food object on the game grid.

        Parameters:
        width (int): The width of the game grid.
        height (int): The height of the game grid.
        snake_body (list): The coordinates of the snake's body.
        """
        pass
```
## Function description: The function of each function and its input and output parameters need to explain its function and meaning.