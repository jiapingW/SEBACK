from piece import Piece

class Board:
    def __init__(self):
        self.size = 8
        self.pieces = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.captured_pieces = {
            "Player 1": [],
            "Player 2": []
        }

    def get_piece(self, position: tuple[int, int]) -> Piece:
        x, y = position
        return self.pieces[x][y]

    def set_piece(self, position: tuple[int, int], piece: Piece):
        x, y = position
        self.pieces[x][y] = piece

    def get_captured_pieces(self, player_name: str) -> list[Piece]:
        return self.captured_pieces[player_name]

    def set_captured_pieces(self, player_name: str, pieces: list[Piece]):
        self.captured_pieces[player_name] = pieces

    def is_valid_move(self, move: tuple[tuple[int, int], tuple[int, int]]) -> bool:
        from_position, to_position = move
        from_x, from_y = from_position
        to_x, to_y = to_position

        if not self._is_valid_position(from_x, from_y) or not self._is_valid_position(to_x, to_y):
            return False

        piece = self.get_piece(from_position)
        if piece is None:
            return False

        valid_moves = piece.get_valid_moves(self)
        return to_position in valid_moves

    def is_game_over(self) -> bool:
        return self.get_winner() is not None

    def get_winner(self) -> str:
        if len(self.captured_pieces["Player 1"]) >= 3:
            return "Player 1"
        elif len(self.captured_pieces["Player 2"]) >= 3:
            return "Player 2"
        else:
            return None

    def _is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size
