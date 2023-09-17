import unittest
from board import Board
from piece import Piece
from player import Player

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.piece1 = Piece(self.player1)
        self.piece2 = Piece(self.player2)

    def test_set_piece(self):
        self.board.set_piece((0, 0), self.piece1)
        self.assertEqual(self.board.get_piece((0, 0)), self.piece1)

    def test_get_captured_pieces(self):
        self.board.set_captured_pieces(self.player1.get_name(), [self.piece1, self.piece2])
        self.assertEqual(self.board.get_captured_pieces(self.player1.get_name()), [self.piece1, self.piece2])
        self.assertEqual(self.board.get_captured_pieces(self.player2.get_name()), [])

    def test_set_captured_pieces(self):
        self.board.set_captured_pieces(self.player1.get_name(), [self.piece1, self.piece2])
        self.assertEqual(self.board.get_captured_pieces(self.player1.get_name()), [self.piece1, self.piece2])

    def test_is_valid_move(self):
        self.board.set_piece((0, 0), self.piece1)
        self.assertTrue(self.board.is_valid_move(((0, 0), (1, 1))))
        self.assertFalse(self.board.is_valid_move(((0, 0), (2, 2))))
        self.assertFalse(self.board.is_valid_move(((1, 1), (2, 2))))

    def test_is_game_over(self):
        self.assertFalse(self.board.is_game_over())
        self.board.set_captured_pieces(self.player1.get_name(), [self.piece1, self.piece2])
        self.assertTrue(self.board.is_game_over())

    def test_get_winner(self):
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_captured_pieces(self.player1.get_name(), [self.piece1, self.piece2])
        self.assertEqual(self.board.get_winner(), self.player1.get_name())

if __name__ == "__main__":
    unittest.main()
