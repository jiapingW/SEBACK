## functional requirements
```python
[
    {
        "Can control the snake using the arrow keys on my keyboard": [
            "Implement a grid system for the snake to move around",
            "The initial length of the snake is 1",
            "The player controls the moving direction of the snake using the arrow keys",
            "The snake moves one grid per input",
            "The snake continues to move in the last input direction if no new input is received"
        ]
    },
    {
        "The snake grows longer when it eats food": [
            "Randomly generate food on the grid, excluding the grids occupied by the snake",
            "When the snake's head reaches the grid with food, the food disappears",
            "The length of the snake increases by 1 when it eats food",
            "The new length is added at the end of the snake"
        ]
    },
    {
        "The player's score increases when the snake eats food": [
            "Initialize the player's score to 0 at the start of the game",
            "Increase the player's score by 1 each time the snake eats food",
            "Display the current score on the game interface"
        ]
    },
    {
        "The game ends if the snake hits the wall or its own body": [
            "If the snake's head moves to the grid at the edge of the interface, the game ends",
            "If the snake's head moves to any grid occupied by its body, the game ends",
            "Display a game over message when the game ends"
        ]
    },
    {
        "The player can restart the game after it ends": [
            "Provide a restart option in the game over message",
            "Reset the game state including the snake's length and position, score, and food position when the game restarts"
        ]
    }
]
```

## non-functional requirements
```python
[
    {
        "Provide a user-friendly and intuitive interface for controlling the snake": [
            "The game interface should clearly display the grid system, the snake, and the food",
            "The game interface should display the current score and game status",
            "The control instructions should be clearly displayed on the game interface"
        ]
    },
    {
        "Ensure the game runs smoothly without lag": [
            "Optimize the game logic to avoid unnecessary computations",
            "Ensure the game refresh rate is consistent and suitable for a smooth gaming experience",
            "Test the game under different system loads to ensure performance stability"
        ]
    }
]
```

## Anything UNCLEAR
The requirement is clear to me.