from segpt.roles.role import SEAgent
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
)
from segpt.actions.get_folder_name import GETProductName
PROMPT_TEMPLATE = """
# Context
{context}

## Format example
{format_example}
-----
Role: You are an architect; the goal is to design the details of functions and classes. The specific realization of the class mainly includes the description of the functions, member attributes and member functions of the class.Your specific implementation of the function mainly includes descriptions of its functions, types and meanings of inputs and outputs.
Requirement: Fill in the following missing information based on the context, note that all sections are response with code form separately
Max Output: 8192 chars or 2048 tokens. Try to use them up.
Attention: Use '##' to split sections, not '#', and '## <SECTION_NAME>' SHOULD WRITE BEFORE the code and triple quote.

## Class description: The function of each class and its member attributes and member functions need to explain its function and meaning.

"""

FORMAT_EXAMPLE = """
---
## Class description
The `Player` class has the following methods:
- `__init__(self, name: str)`: Initializes a new player with the given name.
  * 'name': player's name 
- `get_name(self) -> str`: Gets the name of the player.
---
"""

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

class Architect_Engineer(SEAgent):
    def __init__(self, name="Bob", profile="Architect engineer", goal="Design the details of functions and classes",
                 constraints=""):
        super().__init__(name, profile, goal, constraints)
        
    def save_detail(self, content):
        with open(GETProductName.docs_path/"detail.md", 'w') as f:
            f.write(content)
            
    def write_detail(self):
        context = ""
        with open(GETProductName.docs_path/"requirement.md", 'r') as f:
            context += f.read()
        with open(GETProductName.docs_path/"system_design.md", 'r') as f:
            context += f.read()
        task_specifier_template = HumanMessagePromptTemplate.from_template(template=PROMPT_TEMPLATE)
        task_specifier_msg = task_specifier_template.format_messages(
            format_example=FORMAT_EXAMPLE,
            context=context,
        )[0]
        specified_task_msg = self.step(task_specifier_msg)
        self.save_detail(specified_task_msg.content)

    def rewrite_detail(self, feedback):
        with open(GETProductName.docs_path/"detail.md", 'r') as f:
            document = f.read()
        task_specifier_template = HumanMessagePromptTemplate.from_template(template=REPROMPT_TEMPLATE)
        task_specifier_msg = task_specifier_template.format_messages(
            context="",
            document=document,
            feedback = feedback
        )[0]
        specified_task_msg = self.step(task_specifier_msg)
        self.save_detail(specified_task_msg.content)
        return task_specifier_msg