from segpt.roles.role import SEAgent
from segpt.actions.write_task import get_write_task, save_task, create_directory_and_file
from segpt.actions.rewrite_task import get_rewrite_task
class ProjectManager(SEAgent):
    def __init__(self, name="Eve", profile="Project Manager",
                 goal="Improve team efficiency and deliver with quality and quantity", constraints=""):
        super().__init__(name, profile, goal, constraints)
    
    def write_task(self):
        task_specifier_msg = get_write_task()
        specified_task_msg = self.step(task_specifier_msg)
        save_task(specified_task_msg)
        create_directory_and_file(specified_task_msg)
    
    def rewrite_task(self, advise):
        task_specifier_msg = get_rewrite_task()
        specified_task_msg = self.step(task_specifier_msg)
        save_task(specified_task_msg)
        create_directory_and_file(specified_task_msg)