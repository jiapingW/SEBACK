import unittest
from unittest.mock import patch
from main import start_game, make_move

class TestMain(unittest.TestCase):
    @patch("main.requests.post")
    def test_start_game(self, mock_post):
        # Mock response data
        mock_data = {
            "game_id": "12345"
        }
        mock_post.return_value.json.return_value = mock_data

        # Test start_game function
        player1 = "Player 1"
        player2 = "Player 2"
        game_id = start_game(player1, player2)

        # Assert the correct API endpoint was called
        mock_post.assert_called_with("http://localhost:8000/game/start", json={"player1": player1, "player2": player2})

        # Assert the correct game ID was returned
        self.assertEqual(game_id, "12345")

    @patch("main.requests.post")
    def test_make_move(self, mock_post):
        # Mock response data
        mock_data = {
            "message": "Move made successfully"
        }
        mock_post.return_value.json.return_value = mock_data

        # Test make_move function
        game_id = "12345"
        player = "Player 1"
        from_x = 1
        from_y = 2
        to_x = 3
        to_y = 4
        message = make_move(game_id, player, from_x, from_y, to_x, to_y)

        # Assert the correct API endpoint was called
        expected_url = "http://localhost:8000/game/12345/move"
        expected_params = {
            "player": player,
            "from_x": from_x,
            "from_y": from_y,
            "to_x": to_x,
            "to_y": to_y
        }
        mock_post.assert_called_with(expected_url, params=expected_params)

        # Assert the correct success message was returned
        self.assertEqual(message, "Move made successfully")

if __name__ == "__main__":
    unittest.main()
