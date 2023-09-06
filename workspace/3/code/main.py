import pygame
from game import Game
from cli import CLI

def main():
    width = 640
    height = 480

    game = Game(width, height)
    cli = CLI(game)

    cli.run()

if __name__ == "__main__":
    main()
