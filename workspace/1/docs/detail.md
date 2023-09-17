## Class description: Player

The `Player` class represents a player in the gokumu game. It has the following member attributes and member functions:

### Member Attributes:
- `name`: A string representing the name of the player.

### Member Functions:
- `__init__(self, name: str)`: Initializes a new player with the given name.
  - `name`: A string representing the name of the player.

- `get_name(self) -> str`: Gets the name of the player.
  - Returns:
    - A string representing the name of the player.

## Class definition:

```python
class Player:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
```

## Example Usage:

```python
# Create a new player
player1 = Player("John")

# Get the name of the player
name = player1.get_name()
print(name)  # Output: "John"
```

In the above example, we create a new player with the name "John" and then retrieve the name using the `get_name()` method. The output will be "John".