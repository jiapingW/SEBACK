from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.prompts.rewrite import PROMPT_TEMPLATE
from segpt.utils.common import CodeParser
from segpt.actions.get_folder_name import GETProductName
from segpt.utils.mermaid import mermaid_to_file
from pathlib import Path

def get_rewrite_design(task):
    # 获取requirement.md和prd.md中的信息进行拼接作为write_design的输入
    with open(GETProductName.docs_path/'prd.md', 'r') as f:
        prd = f.read()
    with open(GETProductName.docs_path/'requirement.md', 'r') as f:
        requirement = f.read()
    with open(GETProductName.docs_path/"design.md", "r") as file:
        document = file.read()
    print('###############\n', prd)
    context = prd + requirement
    
    task_specifier_template = HumanMessagePromptTemplate.from_template(template =PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=context, document = document, feedback = task
    )[0]
    return task_specifier_msg
