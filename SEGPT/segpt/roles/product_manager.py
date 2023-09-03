from segpt.roles.role import SEAgent
from segpt.actions.write_prd import get_write_prd, save_prd
from segpt.actions.rewrite_prd import get_rewrite_prd
from segpt.memory.memory import Memory
from segpt.actions.get_folder_name import GETProductName

class ProductManager(SEAgent):
    def __init__(self, name="Alice", profile="Product Manager", 
                 goal="Efficiently create a successful product",
                 constraints=""):
        super().__init__(name, profile, goal, constraints)
            
    def write_prd(self, task):
        task_specifier_msg = get_write_prd(task)
        specified_task_msg = self.step(task_specifier_msg)
        save_prd(specified_task_msg, True)
        # Memory.set_file_path(str(GETProductName.workspace)+"/memory")
        # self.savemessage([task_specifier_msg, specified_task_msg])
        # print(specified_task_msg)

    def rewrite_prd(self, task):
        #把她的记忆存到一个列表里，用的时候查一下跟现在相关的
        task_specifier_msg = get_rewrite_prd(task)
        specified_task_msg = self.step(task_specifier_msg)
        save_prd(specified_task_msg, False)
        self.savemessage([task_specifier_msg, specified_task_msg])
        print(specified_task_msg)