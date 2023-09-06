from random import randint
from typing import Tuple


class Food:
    def __init__(self):
        self.position = (0, 0)

    def generate_position(self, grid_size: Tuple[int, int]) -> Tuple[int, int]:
        max_x, max_y = grid_size
        x = randint(0, max_x - 1)
        y = randint(0, max_y - 1)
        self.position = (x, y)
        return self.position
