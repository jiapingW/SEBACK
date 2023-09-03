from typing import List, Tuple
PROMPT_TEMPLATE = """
# Context
## Original Requirements
{requirements}

## Format example
{format_example}
-----
Role: You are a professional product manager; the goal is to design a concise, usable, efficient product
Requirements: According to the context, fill in the following missing information, note that each sections are returned in Python code triple quote form seperatedly. If the requirements are unclear, ensure minimum viability and avoid excessive design
ATTENTION: Use '##' to SPLIT SECTIONS, not '#'. AND '## <SECTION_NAME>' SHOULD WRITE BEFORE the code and triple quote. Output carefully referenced "Format example" in format.

## Original Requirements: Provide as Plain text, place the polished complete original requirements here

## Product Goals: Provided as Python list[str], up to 3 clear, orthogonal product goals. If the requirement itself is simple, the goal should also be simple

## User Stories: Provided as Python list[str], up to 5 scenario-based user stories, If the requirement itself is simple, the user stories should also be less

## Requirement Analysis: Provide as Plain text. Be simple. LESS IS MORE. Make your requirements less dumb. Delete the parts unnessasery.

## Requirement Pool: Provided as Python list[str, str], the parameters are requirement description, priority(P0/P1/P2), respectively, comply with PEP standards; no more than 5 requirements and consider to make its difficulty lower

## Anything UNCLEAR: Provide as Plain text. Make clear here.
"""
FORMAT_EXAMPLE = """
---
## Original Requirements
The boss ...

## Product Goals
```python
[
    "Create a ...",
]
```

## User Stories
```python
[
    "As a user, ...",
]
```

## Requirement Analysis
The product should be a ...

## Requirement Pool
```python
[
    ("End game ...", "P0")
]
```

## Anything UNCLEAR
There are no unclear points.
---
"""
OUTPUT_MAPPING = {
    "Original Requirements": (str, ...),
    "Product Goals": (List[str], ...),
    "User Stories": (List[str], ...),
    "Requirement Analysis": (str, ...),
    "Requirement Pool": (List[Tuple[str, str]], ...),
    "Anything UNCLEAR": (str, ...),
}