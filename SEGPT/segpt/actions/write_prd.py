from segpt.prompts.prd import PROMPT_TEMPLATE, FORMAT_EXAMPLE
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import get_product_name, GETProductName
from segpt.utils.common import CodeParser


def save_prd(prd_content, is_first_save=True):
    content = prd_content.content
    with open(GETProductName.docs_path/"prd.md", "w") as f:
        f.write(content)


# 获取write_prd的prompt
def get_write_prd(task):
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        requirements=task, format_example=FORMAT_EXAMPLE
    )[0]
    return task_specifier_msg
