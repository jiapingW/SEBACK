import unittest
from unittest.mock import patch
from gokumu_game.utils import get_valid_moves
from gokumu_game.board import Board
from gokumu_game.player import Player
from gokumu_game.piece import Piece

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def test_get_valid_moves_no_moves(self):
        # Set up the board with no pieces
        self.board.set_piece((0, 0), None)
        self.board.set_piece((0, 1), None)
        self.board.set_piece((1, 0), None)
        self.board.set_piece((1, 1), None)

        valid_moves = get_valid_moves(self.board, self.player1)
        self.assertEqual(valid_moves, [])

    def test_get_valid_moves_single_piece(self):
        # Set up the board with a single piece
        piece = Piece(self.player1.get_name())
        self.board.set_piece((0, 0), piece)

        valid_moves = get_valid_moves(self.board, self.player1)
        expected_moves = [((0, 0), (1, 1)), ((0, 0), (1, 0)), ((0, 0), (0, 1))]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_multiple_pieces(self):
        # Set up the board with multiple pieces
        piece1 = Piece(self.player1.get_name())
        piece2 = Piece(self.player2.get_name())
        self.board.set_piece((0, 0), piece1)
        self.board.set_piece((0, 1), piece2)

        valid_moves = get_valid_moves(self.board, self.player1)
        expected_moves = [((0, 0), (1, 1)), ((0, 0), (1, 0)), ((0, 0), (0, 1))]
        self.assertEqual(valid_moves, expected_moves)

    def test_get_valid_moves_invalid_piece(self):
        # Set up the board with an invalid piece
        piece = Piece("Invalid player")
        self.board.set_piece((0, 0), piece)

        valid_moves = get_valid_moves(self.board, self.player1)
        self.assertEqual(valid_moves, [])

if __name__ == "__main__":
    unittest.main()
