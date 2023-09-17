from board import Board
from player import Player
from ai import AI
from utils import get_valid_moves

class Game:
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.ai = None

    def start_game(self, player1_name: str, player2_name: str):
        self.board = Board()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.ai = AI()

    def make_move(self, player_name: str, from_x: int, from_y: int, to_x: int, to_y: int) -> str:
        player = self._get_player_by_name(player_name)
        if player is None:
            return "Invalid player"

        piece = self.board.get_piece((from_x, from_y))
        if piece is None:
            return "Invalid piece"

        valid_moves = get_valid_moves(self.board, player)
        move = ((from_x, from_y), (to_x, to_y))
        if move not in valid_moves:
            return "Invalid move"

        self.ai.make_move(player, move)
        self.board.set_piece((to_x, to_y), piece)
        self.board.set_piece((from_x, from_y), None)

        return "Move made successfully"

    def _get_player_by_name(self, player_name: str) -> Player:
        if self.player1.get_name() == player_name:
            return self.player1
        elif self.player2.get_name() == player_name:
            return self.player2
        else:
            return None

    def is_game_over(self) -> bool:
        return self.board.is_game_over()

    def get_winner(self) -> Player:
        if self.is_game_over():
            return self.board.get_winner()
        else:
            return None
