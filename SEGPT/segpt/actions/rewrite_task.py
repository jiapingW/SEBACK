from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.utils.common import CodeParser
from segpt.actions.get_folder_name import GETProductName
from segpt.utils.mermaid import mermaid_to_file
from pathlib import Path



REPROMPT_TEMPLATE = """
# Context
{context}

# Doucment
{document}

# Feedback
{feedback}
-----
Your task now is to revise the 'Doucment' in accordance with the 'Feedback'. 
Make sure to address the Feedback adequately while maintaining the format of the document.
Attention: Only return the content of modified document, begining with '##', not '#'
"""

def get_rewrite_task(advise):
    # 获取requirement.md和prd.md中的信息进行拼接作为write_design的输入
    with open(GETProductName.docs_path/'task.md', 'r') as f:
        document = f.read()
    context = ""
    
    task_specifier_template = HumanMessagePromptTemplate.from_template(template =REPROMPT_TEMPLATE)
    task_specifier_msg = task_specifier_template.format_messages(
        context=context, document = document, feedback = advise
    )[0]
    return task_specifier_msg
