## game.py

import curses
from snake import Snake
from food import Food

class Game:
    def __init__(self, width: int = 20, height: int = 20):
        """
        Initializes a new game with the given width and height.
        Creates a new Snake and Food object.
        Initializes the score to 0.

        Attributes:
        width (int): The width of the game grid.
        height (int): The height of the game grid.
        score (int): The current score of the game.
        snake (Snake): The snake controlled by the player.
        food (Food): The food object in the game.
        """
        self.width = width
        self.height = height
        self.score = 0
        self.snake = Snake()
        self.food = Food()
        self.food.generate(self.width, self.height, self.snake.body)

    def start(self):
        """
        Starts the game. The snake starts moving based on the player's input.
        """
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.timeout(100)
        self.window.keypad(1)
        self.window.addch(self.food.position[1], self.food.position[0], '#')

    def end(self):
        """
        Ends the game. Displays a game over message and the player's final score.
        """
        self.window.addstr(int(self.height/2), int(self.width/2), "Game Over!")
        self.window.refresh()
        curses.napms(2000)
        curses.endwin()

    def restart(self):
        """
        Restarts the game. Resets the game state including the snake's length and position, score, and food position.
        """
        self.__init__(self.width, self.height)
        self.start()

    def update(self):
        """
        Updates the game state. Moves the snake, checks for collisions, generates food, and updates the score.
        """
        event = self.window.getch()
        self.snake.move(event)

        if self.snake.collides_with_self() or self.snake.collides_with_wall(self.width, self.height):
            self.end()

        if self.snake.body[0] == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.generate(self.width, self.height, self.snake.body)
        else:
            self.snake.move()

        self.window.clear()
        self.window.addstr(0, 0, "Score: " + str(self.score) + ' ')
        self.window.addch(self.food.position[1], self.food.position[0], '#')
        for body_part in self.snake.body:
            self.window.addch(body_part[1], body_part[0], '*')
        self.window.refresh()
