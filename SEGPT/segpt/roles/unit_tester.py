from segpt.roles.role import SEAgent
from segpt.actions.write_test import get_write_test, save_test_code
from segpt.actions.rewrite_test import get_rewrite_test


class Tester(SEAgent):
    def __init__(self, name="Mary", profile="Tester", goal="Write comprehensive and robust tests to ensure codes will work as expected without bugs",
                 constraints="The test code you write should conform to code standard like PEP8, be modular, easy to read and maintain"): 
        super().__init__(name, profile, goal, constraints)
        self.test_code_list: list[str] = []  # 存放测试生成的代码的文件名列表，前缀包含test_
        
    def write_test(self, test_file_list: list[str]):
        task_specifier_msg_dict = get_write_test(test_file_list)
        for test_filename in task_specifier_msg_dict.keys():
            codetxt = self.step(task_specifier_msg_dict[test_filename])
            save_test_code(test_filename, codetxt.content)
        self.test_code_list = list(task_specifier_msg_dict.keys())
        
    def rewrite_test(self, advice: str, filename: str):
        engineer_prompt_msg1 = get_rewrite_test(filename, advice)
        codetxt = self.step(engineer_prompt_msg1)
        save_test_code(filename, codetxt.content)
        
        