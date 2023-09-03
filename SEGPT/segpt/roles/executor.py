from segpt.actions.get_folder_name import GETProductName
import subprocess


class Executor:
    def __init__(self) -> None:
        self.error_message = ""
        self.path: str = None  # 测试的代码所在的目录
       
    # 更新test路径
    def setPath(self):
        self.path = GETProductName.test_case_path

    def run(self):
        cd_command = "cd " + self.path+";"
        # # dir = GETProductName.test_case_path  # 测试的代码所在的目录
        # cd_command = "cd " + str(dir)+";"  # 到test_case目录下
        p = subprocess.Popen(cd_command + "python user.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        std_out, std_err = p.communicate()
        if len(std_err) == 0:
            print("test pass.")
        else:
            self.error_message = std_err
            print('there is a error need to revise.')
        p.wait(2)
        if p.poll() == 0:
            print("Success")