import random

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
