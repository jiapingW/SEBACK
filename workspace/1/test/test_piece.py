import unittest
from piece import Piece

class TestPiece(unittest.TestCase):
    def test_get_owner(self):
        player = "Player 1"
        piece = Piece(player)
        self.assertEqual(piece.get_owner(), player)

    def test_get_type(self):
        player = "Player 1"
        piece = Piece(player)
        self.assertEqual(piece.get_type(), "Piece")

if __name__ == "__main__":
    unittest.main()
