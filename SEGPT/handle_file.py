from segpt.actions.get_folder_name import get_product_name, GETProductName, set_product_name
from segpt.actions.write_code import get_file_list
import os
from manager import Manager
import pickle


class HandleFile:
    # project_name_to_id = {}
    project_id_to_name = {}
    project_id_path = {}
    manager = Manager()
    trash = {}
    id: int = 1
        
    def get_file_content(self, filepath: str):
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    
    def get_all_python_files(self, dir: str):
        file_names = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    file_names.append(file_path)
        return file_names
    
    def get_code_by_filename(self, filename: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        file_content = self.get_file_content(filepath+"/code/"+filename+".py")
        return file_content
    
    def get_unittest_by_filename(self, filename: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        file_content = self.get_file_content(filepath+"/test/"+filename+".py")
        return file_content
    
    # classification只能为detail、prd、requirement、system_design、task、data_api_design、seq_flow
    def get_docs_by_classification(self, classification: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        if classification in ['detail', 'prd', 'requirement', 'system_design', 'task']:    
            file_content = self.get_file_content(filepath+"/docs/"+classification+".md")
            return file_content
        elif classification in ['data_api_design', 'seq_flow']:
            file_content = self.get_file_content(filepath+"/resources/"+classification+".mmd")
            return file_content
    
    def write_docs_file(self, content: str, classification: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        with open(filepath+"/docs/"+classification+".md", 'w') as f:
            f.write(content)
    
    def write_code_file(self, content: str, filename: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        with open(filepath+"/code/"+filename+".py", 'w') as f:
            f.write(content)

    def write_unittest_file(self, content: str, filename: str, tid: int):
        filepath = HandleFile.project_id_path[tid]
        with open(filepath+"/test/"+filename+".py", 'w') as f:
            f.write(content)
            
    def rewrite_file(self, advise: str, filename: str, tid: int):
        set_product_name(tid)
        if filename == 'prd':
            self.manager.product_manager.rewrite_prd(advise)
        elif filename == 'requirement':
            self.manager.requirement_engineer.rewrite_req(advise)
        elif filename == 'system_design':
            self.manager.architect.rewrite_design(advise)
        elif filename == 'task':
            self.manager.project_manager.rewrite_task(advise)
        elif filename == 'detail':
            self.manager.architect_engineer.rewrite_detail(advise)
        elif 'test_' in filename:
            self.manager.tester.rewrite_test(advise, filename+".py")
        else:
            self.manager.engineer.rewrite_code(advise, filename+".py")
    
    def first_generate_prd(self, tid: int, idea: str):
        get_product_name(tid)
        self.manager.product_manager.write_prd(idea)
        
    def retry_prd(self, tid: int):
        idea = self.project_id_to_name[tid]
        get_product_name(tid)
        self.manager.product_manager.write_prd(idea)
        
    def generate_docx(self, filename: str, tid: int):
        set_product_name(tid)
        if filename == 'requirement':
            self.manager.requirement_engineer.write_req()
        elif filename == 'system_design':
            self.manager.architect.write_design()
        elif filename == 'task':
            self.manager.project_manager.write_task()
        elif filename == 'detail':
            self.manager.architect_engineer.write_detail()
        else:
            pass
             
    def generate_code(self, tid: int):
        set_product_name(tid)
        self.manager.engineer.write_code()
        self.manager.engineer.code_memory = [] # 清空代码缓存
                
    def get_filetree(self, path: str):
        # print("path:     ", path)
        if os.path.isdir(path):
            filetree = {'type': 'directory', 'name': os.path.basename(path), 'children': []}
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                filetree['children'].append(self.get_filetree(item_path))
            return filetree
        else:
            return {'type': 'file', 'name': os.path.basename(path)}
    
    def get_filetree_by_id(self, tid: int):
        filepath = HandleFile.project_id_path[tid]
        filetree = self.get_filetree(filepath)
        filetree["name"] = HandleFile.project_id_to_name[tid]
        return filetree
        
    def generate_unittest(self, tid: int):
        set_product_name(tid)
        self.manager.tester.write_test(get_file_list())
        
        
# 从txt中加载之前的项目信息
def load_parameter():
    if os.path.exists('id_to_name.txt'):
        with open('id_to_name.txt', 'rb') as f:
            HandleFile.project_id_to_name = pickle.load(f)
    # if os.path.exists('name_to_id.txt'):
    #     with open('name_to_id.txt', 'rb') as f:
    #         HandleFile.project_name_to_id = pickle.load(f)
    if os.path.exists('id_to_path.txt'):
        with open('id_to_path.txt', 'rb') as f:
            HandleFile.project_id_path = pickle.load(f)
    if os.path.exists('id.txt'):
        with open('id.txt', 'rb') as f:
            HandleFile.id = pickle.load(f)
    if os.path.exists('trash.txt'):
        with open('trash.txt', 'rb') as f:
            HandleFile.trash = pickle.load(f)
    
    
def create_projectMap(project_name: str):
    load_parameter()
    get_product_name(HandleFile.id)
    HandleFile.project_id_to_name[HandleFile.id] = project_name
    # HandleFile.project_name_to_id[project_name] = HandleFile.id
    HandleFile.project_id_path[HandleFile.id] = str(GETProductName.workspace)
    HandleFile.id += 1
    with open('id_to_name.txt', 'wb') as f:
        pickle.dump(HandleFile.project_id_to_name, f)
    # with open('name_to_id.txt', 'wb') as f:
    #     pickle.dump(HandleFile.project_name_to_id, f)
    with open('id_to_path.txt', 'wb') as f:
        pickle.dump(HandleFile.project_id_path, f)
    with open('id.txt', 'wb') as f:
        pickle.dump(HandleFile.id, f)
    return HandleFile.id-1
    

def get_filepath_by_id(tid: int):
    return HandleFile.project_id_path[tid]
    
        
def get_all_projects():
    return list(HandleFile.project_id_path.keys)


def update_name(id: int, new_name: str):
    HandleFile.project_id_to_name[id] = new_name
    with open('id_to_name.txt', 'wb') as f:
        pickle.dump(HandleFile.project_id_to_name, f)
    return id


def delete_project(id: int):
    HandleFile.trash[id] = HandleFile.project_id_to_name[id]
    with open('trash.txt', 'wb') as f:
        pickle.dump(HandleFile.trash, f)
    del HandleFile.project_id_to_name[id]
    with open('id_to_name.txt', 'wb') as f:
        pickle.dump(HandleFile.project_id_to_name, f)


def recover_project(id: int):
    HandleFile.project_id_to_name[id] = HandleFile.trash[id]
    print(HandleFile.project_id_to_name)
    del HandleFile.trash[id]
    with open('trash.txt', 'wb') as f:
        pickle.dump(HandleFile.trash, f)
    with open('id_to_name.txt', 'wb') as f:
        pickle.dump(HandleFile.project_id_to_name, f)
    