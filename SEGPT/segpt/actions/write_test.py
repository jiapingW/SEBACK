# from segpt.actions.get_folder_name import GETProductName
# from langchain.prompts.chat import (
#     HumanMessagePromptTemplate,
# )
# from segpt.prompts.test_case import PROMPT_TEMPLATE
# from segpt.utils.common import CodeParser


# 此版本对应的tester为role中的tester以及prompt中的test_case.py
# def save_test_code(test_file_id: int, codetxt: str):
#     code = CodeParser.parse_code(block="", text=codetxt)
#     with open(str(GETProductName.test_case_path)+"/"+str(test_file_id)+".py", 'w') as f:
#         f.write(code)
    

# # codefilelist中的元素包含文件后缀名.py
# def get_write_test(codefilelist: list[str], user_requirements: str, test_file_id: int):
#     # 目前实现只从Engineer和用户处获取
#     filename_and_code_to_test = ""
#     for codefilename in codefilelist:
#         with open(str(GETProductName.code_path)+"/"+codefilename, 'r') as f:
#             code = f.read()
#             filename_and_code_to_test += codefilename+"\n"+code+"\n"
            
#     task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
#     task_specifier_msg = task_specifier_template.format_messages(
#         user_requirements=user_requirements, 
#         filename_and_code_to_test=filename_and_code_to_test,
#         workspace=str(GETProductName.workspace),
#         test_file_name=str(test_file_id)+".py"
#     )[0]
#     return task_specifier_msg

from segpt.prompts.test import PROMPT_TEMPLATE
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import GETProductName
from segpt.utils.common import CodeParser


def save_test_code(test_file_name: str, codetxt: str):
    code = CodeParser.parse_code(block="", text=codetxt)
    with open(str(GETProductName.test_case_path)+"/"+test_file_name, 'w') as f:
        f.write(code)


# 返回一个dict，是不同的test_filename及其prompt的kv对构成的, 目前没有考虑user_requirements加入prompt
def get_write_test(codefilelist: list[str]):
    res = {}
    task_specifier_template = HumanMessagePromptTemplate.from_template(template = PROMPT_TEMPLATE)
    with open(str(GETProductName.docs_path)+"/system_design.md", 'r') as f:
        system_design = f.read()
    with open(str(GETProductName.docs_path)+"/task.md", 'r') as f:
        task = f.read()
    # 目前实现只从Engineer和system design和task处获取
    filename_and_code_to_test = ""
    for codefilename in codefilelist:
        with open(str(GETProductName.code_path)+"/"+codefilename, 'r') as f:
            code = f.read()
            filename_and_code_to_test += codefilename+":\n ```python\n ... "+code+"\n```"
    for filename in codefilelist:
        test_filename = "test_"+filename
        print(test_filename)
        task_specifier_msg = task_specifier_template.format_messages(
            filename=filename,
            system_design=system_design,
            task=task,
            code=filename_and_code_to_test,
            workspace=str(GETProductName.workspace),
            test_file_name=test_filename
        )[0]
        res[test_filename] = task_specifier_msg
    return res
    