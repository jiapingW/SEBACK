import unittest
from player import Player
from piece import Piece

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        player = Player("Player 1")
        self.assertEqual(player.get_name(), "Player 1")

    def test_get_pieces(self):
        player = Player("Player 1")
        piece1 = Piece("Player 1")
        piece2 = Piece("Player 1")
        player.set_pieces([piece1, piece2])
        self.assertEqual(player.get_pieces(), [piece1, piece2])

    def test_set_pieces(self):
        player = Player("Player 1")
        piece1 = Piece("Player 1")
        piece2 = Piece("Player 1")
        player.set_pieces([piece1, piece2])
        self.assertEqual(player.get_pieces(), [piece1, piece2])

if __name__ == "__main__":
    unittest.main()
