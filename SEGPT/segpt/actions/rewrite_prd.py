from segpt.prompts.rewrite import PROMPT_TEMPLATE
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import get_product_name, GETProductName
from segpt.utils.common import CodeParser

# 获取write_prd的prompt
def get_rewrite_prd(task):
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)

    filename = GETProductName.docs_path/"prd.md"
    with open(filename, "r") as file:
        document = file.read()
    
    task_specifier_msg = task_specifier_template.format_messages(
        context="", document = document, feedback = task
    )[0]
    return task_specifier_msg
