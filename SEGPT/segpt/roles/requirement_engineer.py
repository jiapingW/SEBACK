from segpt.roles.role import SEAgent
from segpt.actions.write_requirement import get_write_req, save_requirements
from segpt.actions.rewrite_requirement import get_rewrite_req


class RequirementEngineer(SEAgent):
    def __init__(self, name="Jack", profile="requirement engineer", goal="generate functional requirements and non-functional requirements with detailed content, clear logic, accurate expression and no redundant information",
                 constraints=""):
        super().__init__(name, profile, goal, constraints)

    def write_req(self):
        task_specifier_msg = get_write_req()
        specified_task_msg = self.step(task_specifier_msg)
        save_requirements(specified_task_msg)
        self.savemessage([task_specifier_msg, specified_task_msg])

    def rewrite_req(self, task):
        task_specifier_msg = get_rewrite_req(task)
        specified_task_msg = self.step(task_specifier_msg)
        save_requirements(specified_task_msg)
        self.savemessage([task_specifier_msg, specified_task_msg])