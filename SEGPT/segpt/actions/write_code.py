from segpt.prompts.code import PROMPT_TEMPLATE
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import GETProductName
from segpt.utils.common import CodeParser


# 从包含code的txt中提取符合要求的code
def parse_code(code_txt: str) -> str:
    return CodeParser.parse_code(block="", text=code_txt)


# filename中包含文件后缀名.py
def save_code(filename: str, code: str):
    print(filename)
    with open(str(GETProductName.code_path)+"/"+filename, "w") as f:
        f.write(code)


# 返回的是一个完整的prompt dict，因为存在多个python 的code文件需要写入,结构是{filename:prompt}
def get_write_code(filename: str, code_memory: list[str] = None):
    # 目前实现只从Architect和Project Manager处获取
    with open(GETProductName.docs_path/'system_design.md', 'r') as f:
        system_design = CodeParser.parse_block(block="Program call flow", text=f.read())
    with open(GETProductName.docs_path/'task.md', 'r') as f:
        task = f.read()
    with open(GETProductName.docs_path/'detail.md', 'r') as f:
        detail = f.read()
    # 如果code_memory不为空，则context中需要加入code_memory的内容
    codeMemory = "\n"
    if code_memory is not None:
        for code in code_memory:
            codeMemory += code
    # fileList = CodeParser.parse_file_list(block="Task list", text=task)  # 从task.md中将File list提取出来构建成list
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
            context=system_design+task+detail+codeMemory, filename=filename
    )[0]
    return task_specifier_msg
    # task_specifier_msg_dict = {}
    # for filename in fileList:
    #     task_specifier_msg = task_specifier_template.format_messages(
    #         context=system_design+task+codeMemory, filename=filename
    #     )[0]
    #     task_specifier_msg_dict[filename] = task_specifier_msg
    # return task_specifier_msg_dict


def get_file_list():
    with open(GETProductName.docs_path/'task.md', 'r') as f:
        task = f.read()
    fileList = CodeParser.parse_file_list(block="Task list", text=task)  # 从task.md中将File list提取出来构建成list
    return fileList