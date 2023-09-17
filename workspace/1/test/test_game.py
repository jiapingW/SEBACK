import unittest
from game import Game
from board import Board
from player import Player
from ai import AI
from utils import get_valid_moves

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.board = Board()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.ai = AI()

    def test_start_game(self):
        self.game.start_game("Player 1", "Player 2")
        self.assertEqual(self.game.player1.get_name(), "Player 1")
        self.assertEqual(self.game.player2.get_name(), "Player 2")

    def test_make_move(self):
        self.game.start_game("Player 1", "Player 2")
        self.board.set_piece((1, 2), self.player1.get_pieces()[0])
        self.board.set_piece((3, 4), None)
        self.assertEqual(self.game.make_move("Player 1", 1, 2, 3, 4), "Move made successfully")
        self.assertEqual(self.board.get_piece((1, 2)), None)
        self.assertEqual(self.board.get_piece((3, 4)), self.player1.get_pieces()[0])

    def test_make_move_invalid_player(self):
        self.game.start_game("Player 1", "Player 2")
        self.assertEqual(self.game.make_move("Invalid Player", 1, 2, 3, 4), "Invalid player")

    def test_make_move_invalid_piece(self):
        self.game.start_game("Player 1", "Player 2")
        self.assertEqual(self.game.make_move("Player 1", 1, 2, 3, 4), "Invalid piece")

    def test_make_move_invalid_move(self):
        self.game.start_game("Player 1", "Player 2")
        self.board.set_piece((1, 2), self.player1.get_pieces()[0])
        self.assertEqual(self.game.make_move("Player 1", 1, 2, 3, 4), "Invalid move")

    def test_get_winner(self):
        self.game.start_game("Player 1", "Player 2")
        self.board.set_captured_pieces("Player 1", [self.player1.get_pieces()[0], self.player1.get_pieces()[1], self.player1.get_pieces()[2]])
        self.assertEqual(self.game.get_winner(), "Player 1")

    def test_get_winner_no_winner(self):
        self.game.start_game("Player 1", "Player 2")
        self.assertEqual(self.game.get_winner(), None)

    def test_get_valid_moves(self):
        self.game.start_game("Player 1", "Player 2")
        self.board.set_piece((1, 2), self.player1.get_pieces()[0])
        valid_moves = get_valid_moves(self.board, self.player1)
        self.assertEqual(valid_moves, [((1, 2), (3, 4)), ((1, 2), (3, 2))])

if __name__ == "__main__":
    unittest.main()
