## ai.py

from board import Board
from player import Player
from utils import get_valid_moves

class AI:
    def __init__(self):
        pass

    def get_move(self, board: Board, player: Player) -> tuple[tuple[int, int], tuple[int, int]]:
        valid_moves = get_valid_moves(board, player)
        return valid_moves[0] if valid_moves else None

    def make_move(self, player: Player, move: tuple[tuple[int, int], tuple[int, int]]):
        from_position, to_position = move
        from_x, from_y = from_position
        to_x, to_y = to_position

        piece = self.board.get_piece(from_position)
        if piece is None:
            return

        self.board.set_piece(to_position, piece)
        self.board.set_piece(from_position, None)
