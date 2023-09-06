import pygame

class GameScreen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")

    def draw_snake(self, snake: Snake) -> None:
        for segment in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0] * 20, segment[1] * 20, 20, 20))

    def draw_food(self, food: Food) -> None:
        pygame.draw.rect(self.screen, (255, 0, 0), (food.position[0] * 20, food.position[1] * 20, 20, 20))

    def draw_score(self, score: int) -> None:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def draw_game_over(self) -> None:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, text_rect)

    def update(self) -> None:
        pygame.display.update()
