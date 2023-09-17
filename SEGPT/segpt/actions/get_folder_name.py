from const import WORKSPACE_ROOT, recreate_workspace


class GETProductName:
    workspace = WORKSPACE_ROOT
    resources_path = ""
    docs_path = ""
    code_path = ""
    test_path = ""
    
    
def get_product_name(id: int):
    GETProductName.workspace = WORKSPACE_ROOT / str(id)
    recreate_workspace(GETProductName.workspace)  # 创建project文件夹
    GETProductName.docs_path = GETProductName.workspace / 'docs' 
    GETProductName.docs_path.mkdir(parents=True, exist_ok=True)  # 创建workspace/1/docs文件夹
    GETProductName.resources_path = GETProductName.workspace / 'resources'
    GETProductName.resources_path.mkdir(parents=True, exist_ok=True)  # 创建workspace/1/resources文件夹
    GETProductName.code_path = GETProductName.workspace / 'code'
    GETProductName.code_path.mkdir(parents=True, exist_ok=True) # 创建workspace/1/code文件夹，存放生成的源代码
    GETProductName.test_path = GETProductName.workspace / 'test'
    GETProductName.test_path.mkdir(parents=True, exist_ok=True)


def set_product_name(id: int):
    GETProductName.workspace = WORKSPACE_ROOT / str(id)
    GETProductName.docs_path = GETProductName.workspace / 'docs' 
    GETProductName.resources_path = GETProductName.workspace / 'resources'
    GETProductName.code_path = GETProductName.workspace / 'code'
    GETProductName.test_path = GETProductName.workspace / 'test'