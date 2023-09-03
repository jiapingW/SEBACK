from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.prompts.rewrite import PROMPT_TEMPLATE
from segpt.actions.get_folder_name import GETProductName

# 获取write_req的prompt
def get_rewrite_req(task):
    with open(GETProductName.docs_path/'prd.md', 'r') as f:
        prd = f.read()
    with open(GETProductName.docs_path/"requirement.md", "r") as file:
        document = file.read()
    
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=prd, document = document, feedback = task
    )[0]
    return task_specifier_msg

