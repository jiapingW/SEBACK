from segpt.roles.role import SEAgent
from segpt.actions.write_code import get_write_code, save_code, parse_code, get_file_list
from segpt.actions.rewrite_code import get_rewrite_code

class Engineer(SEAgent):
    def __init__(self, name="Alex", profile="Engineer", goal="Write elegant, readable, extensible, efficient code",
        constraints="The code you write should conform to code standard like PEP8, be modular, easy to read and maintain"):
        super().__init__(name, profile, goal, constraints)
        self.filelist = []
        self.code_memory = [] # 因为engineer并不是一个个体，所以他需要有自己特殊的memory来存储当前轮中所有的对话
    
    def write_code(self):
        self.filelist = get_file_list()
        for filename in self.filelist:
            engineer_prompt_msg = get_write_code(filename, self.code_memory)
            specified_task_msg = self.step(engineer_prompt_msg)
            code = parse_code(specified_task_msg.content)
            # 将生成的code与文件名进行拼接存入到code_memory中
            self.code_memory.append("## Code:"+filename+":\n ```python\n ... "+code+"\n```")
            save_code(filename, code)
    
    def rewrite_code(self, advice: str, filename: str):
        engineer_prompt_msg1 = get_rewrite_code(filename, advice)
        specified_task_msg = self.step(engineer_prompt_msg1)
        code = parse_code(specified_task_msg.content)
        save_code(filename, code)