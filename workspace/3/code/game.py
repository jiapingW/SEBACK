import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, width: int, height: int):
        """
        Initializes a new game with the specified width and height.

        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height))
        self.snake = Snake(width // 2, height // 2)
        self.food = Food(0, 0)
        self.score = 0

    def update(self) -> None:
        """
        Updates the game state.
        """
        self.snake.move()

        if self.snake.collides_with_food(self.food):
            self.snake.grow()
            self.score += 1
            self.food = self.generate_food()

        if self.snake.collides_with_self() or self.snake.collides_with_boundary(self.width, self.height):
            self.end_game()

    def handle_input(self) -> None:
        """
        Handles user input.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.dy != 1:
                    self.snake.dx = 0
                    self.snake.dy = -1
                elif event.key == pygame.K_DOWN and self.snake.dy != -1:
                    self.snake.dx = 0
                    self.snake.dy = 1
                elif event.key == pygame.K_LEFT and self.snake.dx != 1:
                    self.snake.dx = -1
                    self.snake.dy = 0
                elif event.key == pygame.K_RIGHT and self.snake.dx != -1:
                    self.snake.dx = 1
                    self.snake.dy = 0

    def draw(self) -> None:
        """
        Draws the game on the surface.
        """
        self.surface.fill((0, 0, 0))
        self.snake.draw(self.surface, 10)
        self.food.draw(self.surface, 10)
        pygame.display.update()

    def run(self) -> None:
        """
        Runs the game loop.
        """
        pygame.init()

        clock = pygame.time.Clock()

        while True:
            self.handle_input()
            self.update()
            self.draw()

            clock.tick(10)

    def generate_food(self) -> Food:
        """
        Generates a new food object at a random position.

        Returns:
            Food: The generated food object.
        """
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return Food(x, y)

    def end_game(self) -> None:
        """
        Ends the game and displays the final score.
        """
        pygame.quit()
        print(f"Game Over! Score: {self.score}")
