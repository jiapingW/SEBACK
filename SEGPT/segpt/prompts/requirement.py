from typing import Dict, List


PROMPT_TEMPLATE = """
Requirement: Fill in the following missing information based on the following context, note that all sections are response with code form separately
Max Output: 8192 chars or 2048 tokens. Try to use them up.
Attention: Use '##' to split sections, not '#', and '## <SECTION_NAME>' SHOULD WRITE BEFORE the code and triple quote.

# Context
{context}

## Format example
{format_example}

## functional requirements: Provide as Python list[dict[str,list[str]]],the keys of the dictionary are are the description of functional requirement，the value of the dictionary is the detailed analysis of the tasks to implement these functional requirements. Each functional requirement is broken down into a maximum of 5. The decomposed task description is required to be clear and logically correct.

## non-functional requirements: Provide as Python list[dict[str,list[str]]],the keys of the dictionary are are the description of non-functional requirement，the value of the dictionary is a breakdown of the tasks to implement these non-functional requirements. Each non-functional requirement is broken down into a maximum of 3. The decomposed task description is required to be clear and logically correct.

## Anything UNCLEAR: Provide as Plain text. Make clear here.


"""

FORMAT_EXAMPLE = """
---
## functional requirements
```python
[
    "Can control the snake using the arrow keys on my keyboard":[The initial length of the snake is 1. 2. and the player controls the moving direction of the snake to make it eat food...",...],
]
```

## non-functional requirements
```python
[
    "Provide a user-friendly and intuitive interface for controlling the snake":["The game interface should contain snakes",...],
]
```

## Anything UNCLEAR
The requirement is clear to me.
---
"""

OUTPUT_MAPPING = {
    "functional requirements": [Dict[str,List[str]],...],
    "non-functional requirements": [Dict[str,List[str]],...],
    "Anything UNCLEAR": (str, ...),
}