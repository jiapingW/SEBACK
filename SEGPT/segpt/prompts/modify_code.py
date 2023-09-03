PROMPT_TEMPLATE = """
Role: You are a professional engineer; the main goal is to write PEP8 compliant, elegant, modular, easy to read and maintain Python 3.9 code.
ATTENTION: Use '##' to SPLIT SECTIONS, not '#'. Output format carefully referenced "Format example".

## Code: Write the code with triple quoto for the file {filename} based on the Program Runtime Error and Source Code.

## Program Runtime Error
{program_runtime_error}

## Source Code
{source_code}
"""