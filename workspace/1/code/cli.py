import curses
from game import Game


class CLI:
    def __init__(self):
        self.game = Game((20, 20))

    def run(self) -> None:
        curses.wrapper(self._run_curses)

    def _run_curses(self, stdscr) -> None:
        stdscr.nodelay(True)
        stdscr.timeout(100)

        while not self.game.game_over:
            key = stdscr.getch()
            self.game.handle_input(key)
            self.game.update()
            self.game.display()

        stdscr.addstr(0, 0, "Game Over!")
        stdscr.refresh()
        stdscr.getch()
