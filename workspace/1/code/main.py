import requests
import json

# API endpoints
START_GAME_URL = "http://localhost:8000/game/start"
MAKE_MOVE_URL = "http://localhost:8000/game/{game_id}/move"

def start_game(player1: str, player2: str) -> str:
    """
    Starts a new game with the given player names.

    Args:
        player1 (str): Name of Player 1.
        player2 (str): Name of Player 2.

    Returns:
        str: ID of the new game.
    """
    payload = {
        "player1": player1,
        "player2": player2
    }
    response = requests.post(START_GAME_URL, json=payload)
    data = response.json()
    game_id = data["game_id"]
    return game_id

def make_move(game_id: str, player: str, from_x: int, from_y: int, to_x: int, to_y: int) -> str:
    """
    Makes a move in the game with the given parameters.

    Args:
        game_id (str): ID of the game.
        player (str): Name of the player making the move.
        from_x (int): X-coordinate of the piece to move.
        from_y (int): Y-coordinate of the piece to move.
        to_x (int): X-coordinate of the destination.
        to_y (int): Y-coordinate of the destination.

    Returns:
        str: Success message.
    """
    url = MAKE_MOVE_URL.format(game_id=game_id)
    params = {
        "player": player,
        "from_x": from_x,
        "from_y": from_y,
        "to_x": to_x,
        "to_y": to_y
    }
    response = requests.post(url, params=params)
    data = response.json()
    message = data["message"]
    return message

if __name__ == "__main__":
    # Start a new game
    game_id = start_game("Player 1", "Player 2")
    print(f"New game started with ID: {game_id}")

    # Make a move
    message = make_move(game_id, "Player 1", 1, 2, 3, 4)
    print(message)
