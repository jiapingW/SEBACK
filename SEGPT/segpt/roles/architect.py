from segpt.roles.role import SEAgent
from segpt.actions.write_design import get_write_design, save_design
from segpt.actions.rewrite_design import get_rewrite_design


class Architect(SEAgent):
    def __init__(self, name="Bob", profile="Architect", goal="Design a concise, usable, complete python system",
                 constraints="Try to specify good open source tools as much as possible"):
        super().__init__(name, profile, goal, constraints)
        
    def write_design(self):
        task_specifier_msg = get_write_design()
        specified_task_msg = self.step(task_specifier_msg)
        save_design(specified_task_msg)
        self.savemessage([task_specifier_msg, specified_task_msg])

    def rewrite_design(self, task):
        task_specifier_msg = get_rewrite_design(task)
        specified_task_msg = self.step(task_specifier_msg)
        save_design(specified_task_msg)
        self.savemessage([task_specifier_msg, specified_task_msg])