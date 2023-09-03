from segpt.roles.role import SEAgent
from segpt.actions.write_test import get_write_test, save_test_code


class Tester(SEAgent):
    def __init__(self, name="Mary", profile="Tester", goal="Write comprehensive and robust tests to ensure codes will work as expected without bugs",
                 constraints="The test code you write should conform to code standard like PEP8, be modular, easy to read and maintain"): 
        super().__init__(name, profile, goal, constraints)
        self.test_file_id: int = 1
    # 生成完测试文件后需要将id+1用于存放下一个文件
    def update_test_file_id(self):
        self.test_file_id += 1
        
    # 到底是生成多个测试文件还是一个测试文件，目前是只生成一个测试文件的
    def write_test_case(self, codefilelist: list[str], case_desc: str):
        task_specifier_msg = get_write_test(codefilelist, case_desc, self.test_file_id)
        test_code = self.step(task_specifier_msg)
        save_test_code(self.test_file_id, test_code.content)
        # 写完文件后更新test_file_id方便后续存储
        self.update_test_file_id()
        
        
    
    