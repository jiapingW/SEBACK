## main.py

import curses
from game import Game

def main(stdscr):
    game = Game(20, 20)
    game.start()
    while True:
        game.update()
        if game.snake.collides_with_self() or game.snake.collides_with_wall(game.width, game.height):
            game.end()
            break

if __name__ == "__main__":
    curses.wrapper(main)
