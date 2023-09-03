from segpt.prompts.task import PROMPT_TEMPLATE, FORMAT_EXAMPLE
from segpt.actions.get_folder_name import GETProductName
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.utils.common import CodeParser
from pathlib import Path


def create_directory_and_file(task: str):
        fileList = CodeParser.parse_file_list(block="Task list", text=task.content)
        for filename in fileList:
            parts = filename.split('/')  # 根据/分割路径
            # 如果只有一个部分，说明没有目录，直接创建文件
            if len(parts) == 1:
                with open(str(GETProductName.code_path)+"/"+filename, 'w') as file:
                    pass  # 创建一个空文件
            else:
                # 从第一个部分开始依次创建目录和文件
                current_path = parts[0]
                for part in parts[1:]:
                    current_path = str(GETProductName.code_path)+"/"+current_path
                    path = Path(current_path)
                    if not path.exists():
                        if '.' in part:  # 如果part中有点，说明是文件名，创建文件
                            with open(current_path, 'w') as file:
                                pass  # 创建一个空文件
                        else:  # 否则创建目录
                            path.mkdir(current_path)


def save_task(task_content):
    content = task_content.content
    with open(GETProductName.docs_path/"task.md", "w") as f:
        f.write(content)


def get_write_task():
    with open(GETProductName.docs_path/'system_design.md', 'r') as f:
        system_design = f.read()
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=system_design, format_example=FORMAT_EXAMPLE
    )[0]
    return task_specifier_msg

