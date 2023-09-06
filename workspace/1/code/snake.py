class Snake:
    def __init__(self, position: Tuple[int, int], direction: Tuple[int, int]):
        self.position = position
        self.direction = direction
        self.body = [position]

    def move(self) -> None:
        x, y = self.position
        dx, dy = self.direction
        new_position = (x + dx, y + dy)
        self.body.insert(0, new_position)
        self.position = new_position
        self.body.pop()

    def grow(self) -> None:
        self.body.append(self.position)

    def collides_with(self, position: Tuple[int, int]) -> bool:
        return position in self.body
