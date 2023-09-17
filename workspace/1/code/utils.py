## utils.py

from board import Board
from player import Player

def get_valid_moves(board: Board, player: Player) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """
    Returns a list of valid moves for the given player on the board.

    Args:
        board (Board): The game board.
        player (Player): The player.

    Returns:
        list[tuple[tuple[int, int], tuple[int, int]]]: A list of valid moves.
    """
    valid_moves = []
    for x in range(board.size):
        for y in range(board.size):
            piece = board.get_piece((x, y))
            if piece is not None and piece.get_player() == player.get_name():
                moves = piece.get_valid_moves(board)
                valid_moves.extend([(from_position, to_position) for from_position, to_position in moves])
    return valid_moves
