import pygame
from snake import Snake
from food import Food
from game_screen import GameScreen

class Game:
    def __init__(self):
        self.score = 0

    def start(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()

        screen_width = 800
        screen_height = 600
        game_screen = GameScreen(screen_width, screen_height)

        snake = Snake()
        food = Food()
        food.generate()

        game_over = False
        game_paused = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_paused = not game_paused

                    if not game_paused:
                        if event.key == pygame.K_UP:
                            snake.change_direction(Snake.UP)
                        elif event.key == pygame.K_DOWN:
                            snake.change_direction(Snake.DOWN)
                        elif event.key == pygame.K_LEFT:
                            snake.change_direction(Snake.LEFT)
                        elif event.key == pygame.K_RIGHT:
                            snake.change_direction(Snake.RIGHT)

            if not game_paused:
                snake.move()

                if snake.collide_with_wall() or snake.collide_with_self():
                    game_over = True

                if snake.head_position() == food.position:
                    snake.eat_food()
                    self.score += 1
                    food.generate()

            game_screen.draw_snake(snake)
            game_screen.draw_food(food)
            game_screen.draw_score(self.score)

            if game_over:
                game_screen.draw_game_over()

            pygame.display.update()
            clock.tick(10)

        pygame.quit()

    def end(self) -> None:
        pass

    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass
