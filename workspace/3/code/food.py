import pygame

class Food:
    def __init__(self, x: int, y: int):
        """
        Initializes a new food with the specified position.

        Args:
            x (int): The x-coordinate of the food's position.
            y (int): The y-coordinate of the food's position.
        """
        self.x = x
        self.y = y

    def draw(self, surface: pygame.Surface, cell_size: int) -> None:
        """
        Draws the food on the given surface using a specific character.

        Args:
            surface (pygame.Surface): The surface to draw the food on.
            cell_size (int): The size of each cell in the grid.
        """
        pygame.draw.rect(surface, (255, 0, 0), (self.x * cell_size, self.y * cell_size, cell_size, cell_size))
