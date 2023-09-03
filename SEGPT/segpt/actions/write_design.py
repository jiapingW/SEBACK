from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.prompts.system_design import PROMPT_TEMPLATE, FORMAT_EXAMPLE
from segpt.utils.common import CodeParser
from segpt.actions.get_folder_name import GETProductName
from segpt.utils.mermaid import mermaid_to_file
from pathlib import Path


def save_design(design_content):
    content = design_content.content
    with open(GETProductName.docs_path/"system_design.md", 'w') as f:
        f.write(content)
    data_api_design = CodeParser.parse_code(block="Data structures and interface definitions", text=content)
    seq_flow = CodeParser.parse_code(block="Program call flow", text=content)
    resources_path = GETProductName.workspace / 'resources'
    print(resources_path)
    mermaid_to_file(data_api_design, resources_path / 'data_api_design')
    mermaid_to_file(seq_flow, resources_path / 'seq_flow')


def get_write_design():
    # 获取requirement.md和prd.md中的信息进行拼接作为write_design的输入
    with open(GETProductName.docs_path/'prd.md', 'r') as f:
        prd = f.read()
    with open(GETProductName.docs_path/'requirement.md', 'r') as f:
        requirement = f.read()
    print('###############\n', prd)
    context = prd + requirement
    
    task_specifier_template = HumanMessagePromptTemplate.from_template(template =PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=context, format_example=FORMAT_EXAMPLE
    )[0]
    return task_specifier_msg
