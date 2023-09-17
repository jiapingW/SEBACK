class Piece:
    def __init__(self, player: str):
        self.player = player

    def get_player(self) -> str:
        return self.player

    def get_valid_moves(self, board) -> list[tuple[int, int]]:
        raise NotImplementedError("Subclasses must implement this method")
