## Implementation approach
We will use the Pygame library to develop the snake game. Pygame is a popular open-source library for creating games in Python and provides a range of functionality for handling graphics, input, and sound. It is well-documented and has a large community, making it a suitable choice for this project.

## Python package name
```python
"snake_game"
```

## File list
```python
[
    "main.py",
]
```

## Data structures and interface definitions
```mermaid
classDiagram
    class Game{
        +score: int
        +start(): None
        +end(): None
        +pause(): None
        +resume(): None
    }

    class Snake{
        +direction: int
        +body: List[Tuple[int, int]]
        +move(): None
        +change_direction(direction: int): None
        +eat_food(): None
        +collide_with_wall(): bool
        +collide_with_self(): bool
    }

    class Food{
        +position: Tuple[int, int]
        +generate(): None
    }

    class GameScreen{
        +width: int
        +height: int
        +draw_snake(snake: Snake): None
        +draw_food(food: Food): None
        +draw_score(score: int): None
        +draw_game_over(): None
    }

    Game "1" -- "1" Snake: has
    Game "1" -- "1" Food: has
    Game "1" -- "1" GameScreen: has
```

## Program call flow
```mermaid
sequenceDiagram
    participant M as Main
    participant G as Game
    participant S as Snake
    participant F as Food
    participant GS as GameScreen

    M->>G: start game
    G->>S: move snake
    G->>F: generate food
    GS->>GS: draw snake
    GS->>GS: draw food
    GS->>GS: draw score
    S->>S: change direction
    S->>S: move
    S->>S: eat food
    S->>S: collide with wall?
    S->>S: collide with self?
    G-->>GS: draw snake
    G-->>GS: draw food
    G-->>GS: draw score
    G-->>GS: draw game over
    M->>G: end game
```

## Anything UNCLEAR
There are no unclear points.