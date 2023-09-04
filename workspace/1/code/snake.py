## snake.py

import random

class Snake:
    def __init__(self):
        """
        Initializes a new snake. The initial length of the snake is 1.

        Attributes:
        body (list): A list of coordinates representing the snake's body.
        direction (str): The current moving direction of the snake.
        """
        self.body = [(0, 0)]
        self.direction = "RIGHT"

    def move(self):
        """
        Moves the snake in the current direction. The snake moves one grid per input.
        """
        head = self.body[0]
        if self.direction == "UP":
            self.body.insert(0, (head[0], head[1] - 1))
        elif self.direction == "DOWN":
            self.body.insert(0, (head[0], head[1] + 1))
        elif self.direction == "LEFT":
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == "RIGHT":
            self.body.insert(0, (head[0] + 1, head[1]))
        self.body.pop()

    def grow(self):
        """
        Increases the length of the snake by 1. The new length is added at the end of the snake.
        """
        self.body.append(self.body[-1])

    def collides_with_self(self) -> bool:
        """
        Checks if the snake collides with its own body.

        Returns:
        bool: True if the snake collides with its own body, False otherwise.
        """
        return len(self.body) != len(set(self.body))

    def collides_with_wall(self, width: int, height: int) -> bool:
        """
        Checks if the snake collides with the wall.

        Parameters:
        width (int): The width of the game grid.
        height (int): The height of the game grid.

        Returns:
        bool: True if the snake collides with the wall, False otherwise.
        """
        head = self.body[0]
        return head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height


class Food:
    def __init__(self):
        """
        Initializes a new food object.

        Attributes:
        position (tuple): The coordinates of the food on the game grid.
        """
        self.position = (0, 0)

    def generate(self, width: int, height: int, snake_body: list):
        """
        Generates a new food object on the game grid.

        Parameters:
        width (int): The width of the game grid.
        height (int): The height of the game grid.
        snake_body (list): The coordinates of the snake's body.
        """
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break
