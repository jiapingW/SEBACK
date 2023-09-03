from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.prompts.requirement import PROMPT_TEMPLATE, FORMAT_EXAMPLE
from segpt.actions.get_folder_name import GETProductName


def save_requirements(requirement_content):
    content = requirement_content.content
    with open(GETProductName.docs_path/"requirement.md", "w") as f:
        f.write(content)


# 获取write_req的prompt
def get_write_req():
    with open(GETProductName.docs_path/'prd.md', 'r') as f:
        prd = f.read()
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=prd, format_example=FORMAT_EXAMPLE
    )[0]
    return task_specifier_msg

