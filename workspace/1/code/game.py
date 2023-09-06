from typing import Tuple
from snake import Snake
from food import Food


class Game:
    def __init__(self, grid_size: Tuple[int, int]):
        self.grid_size = grid_size
        self.score = 0
        self.snake = Snake((grid_size[0] // 2, grid_size[1] // 2), (0, 1))
        self.food = Food()
        self.game_over = False

    def update(self) -> None:
        if not self.game_over:
            self.snake.move()
            if self.snake.collides_with(self.food.position):
                self.snake.grow()
                self.score += 1
                self.food.generate_position(self.grid_size)
            if self.snake.position[0] < 0 or self.snake.position[0] >= self.grid_size[0] or \
                    self.snake.position[1] < 0 or self.snake.position[1] >= self.grid_size[1] or \
                    self.snake.collides_with(self.snake.position):
                self.game_over = True

    def handle_input(self, key: int) -> None:
        if key == 259 and self.snake.direction != (1, 0):
            self.snake.direction = (-1, 0)
        elif key == 258 and self.snake.direction != (-1, 0):
            self.snake.direction = (1, 0)
        elif key == 260 and self.snake.direction != (0, 1):
            self.snake.direction = (0, -1)
        elif key == 261 and self.snake.direction != (0, -1):
            self.snake.direction = (0, 1)

    def display(self) -> None:
        grid = [[' ' for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]
        for segment in self.snake.body:
            grid[segment[0]][segment[1]] = 'X'
        grid[self.snake.position[0]][self.snake.position[1]] = 'O'
        grid[self.food.position[0]][self.food.position[1]] = 'F'
        print('\n'.join([' '.join(row) for row in grid]))

