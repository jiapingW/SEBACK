## food.py

import random

class Food:
    def __init__(self):
        self.position = (0, 0)

    def generate(self) -> None:
        max_x = GameScreen.width - 1
        max_y = GameScreen.height - 1
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        self.position = (x, y)
