class Snake:
    def __init__(self, x: int, y: int):
        """
        Initializes a new snake with the specified head position.

        Args:
            x (int): The x-coordinate of the snake's head position.
            y (int): The y-coordinate of the snake's head position.
        """
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.body = [(x, y)]

    def move(self) -> None:
        """
        Updates the snake's position based on the current movement direction.
        """
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def grow(self) -> None:
        """
        Adds a new body segment to the snake's body.
        """
        self.body.append((self.x, self.y))

    def collides_with_food(self, food) -> bool:
        """
        Checks if the snake's head position overlaps with the food's position.

        Args:
            food (Food): The food object to check collision with.

        Returns:
            bool: True if the snake's head position overlaps with the food's position, False otherwise.
        """
        return (self.x, self.y) == (food.x, food.y)

    def collides_with_self(self) -> bool:
        """
        Checks if the snake's head position overlaps with any part of its body.

        Returns:
            bool: True if the snake's head position overlaps with any part of its body, False otherwise.
        """
        return (self.x, self.y) in self.body[1:]

    def collides_with_boundary(self, width: int, height: int) -> bool:
        """
        Checks if the snake's head position is outside the boundaries of the grid.

        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.

        Returns:
            bool: True if the snake's head position is outside the boundaries of the grid, False otherwise.
        """
        return self.x < 0 or self.x >= width or self.y < 0 or self.y >= height

    def draw(self, surface, cell_size: int) -> None:
        """
        Draws the snake on the given surface using a specific character.

        Args:
            surface (pygame.Surface): The surface to draw the snake on.
            cell_size (int): The size of each cell in the grid.
        """
        for segment in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
