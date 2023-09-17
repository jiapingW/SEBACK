from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import GETProductName


PROMPT_TEMPLATE  = """
NOTICE
Role: You are a professional software engineer. The main objective is to produce PEP8 compliant, elegant, modular, easily readable, and maintainable Python 3.9 code.

ATTENTION
- Use '##' to indicate section splits, not '#'.
- Your output should closely follow the provided "Format example".

1. You must implement this in ONLY ONE FILE. Use the existing API when available. If an API doesn't exist, you should implement it in this file.
2. Requirement: rewrite code according to Advice and Original Code.
3. Attention1: Always provide DEFAULT VALUES for any settings. Use STRONGLY TYPED and EXPLICIT VARIABLES wherever possible.
4. The file will reside in the same folder as your code.
5. Do not define the class in other files; keep all code in this single file.

-----
## Advice
{advice}

## Original Code
{original_code}

## Format example
-----
## Code: {filename}

```python
# Your Python 3.9 code here
```
-----
"""


# 返回的是一个完整的prompt dict，因为存在多个python 的code文件需要写入,结构是{filename:prompt}
def get_rewrite_test(filename: str, advice: str):

    with open(str(GETProductName.test_path)+"/"+filename, 'r') as f:
    # 如果code_memory不为空，则context中需要加入code_memory的内容
        code = f.read()

    task_specifier_template = HumanMessagePromptTemplate.from_template(template=PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        advice=advice, original_code=code, filename=filename
    )[0]
    return task_specifier_msg
  