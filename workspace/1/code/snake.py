## snake.py

from typing import List, Tuple

class Snake:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self):
        self.direction = Snake.RIGHT
        self.body = [(0, 0)]

    def move(self) -> None:
        head = self.body[0]
        x, y = head

        if self.direction == Snake.UP:
            y -= 1
        elif self.direction == Snake.DOWN:
            y += 1
        elif self.direction == Snake.LEFT:
            x -= 1
        elif self.direction == Snake.RIGHT:
            x += 1

        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, direction: int) -> None:
        self.direction = direction

    def eat_food(self) -> None:
        head = self.body[0]
        x, y = head

        if self.direction == Snake.UP:
            y -= 1
        elif self.direction == Snake.DOWN:
            y += 1
        elif self.direction == Snake.LEFT:
            x -= 1
        elif self.direction == Snake.RIGHT:
            x += 1

        self.body.insert(0, (x, y))

    def collide_with_wall(self) -> bool:
        head = self.body[0]
        x, y = head

        if x < 0 or x >= GameScreen.width or y < 0 or y >= GameScreen.height:
            return True

        return False

    def collide_with_self(self) -> bool:
        head = self.body[0]
        x, y = head

        if (x, y) in self.body[1:]:
            return True

        return False

    def head_position(self) -> Tuple[int, int]:
        return self.body[0]
