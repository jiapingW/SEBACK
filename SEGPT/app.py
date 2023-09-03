from flask import Flask, render_template, jsonify, request, redirect
import zipfile
import json
import os
from handle_file import HandleFile, create_projectMap, update_name, load_parameter, delete_project, recover_project
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/create')
# def create():
#     return render_template('create.html')

# @app.route('/edit')
# def edit():
#     return render_template('edit.html')

# @app.route('/generate')
# def generate():
#     return render_template('generate.html')

# @app.route('/edit_generate')
# def edit_generate():
#     return render_template('edit_generate.html')


@app.route('/api/projects', methods=['GET'])
def get_projects():
    load_parameter()
    projects = HandleFile.project_id_to_name
    res = []
    for i in projects.keys():
        res.append({"id": i, "name": projects[i]})
    return jsonify(res), 200


# 从name生成prd
@app.route('/api/project_name', methods=['POST'])
def get_project_name():
    data = request.get_json()
    project_name = data.get('name')
    tid = create_projectMap(project_name)
    handle_file.first_generate_prd(tid, project_name)
    prd = handle_file.get_docs_by_classification("prd", tid)  # 获取prd的内容
    return jsonify({"prd": prd, "id": tid, "name": project_name}), 200


@app.route('/api/update_prd', methods=['POST'])
def create_project():
    # requirment.md确认完成
    data = request.get_json()
    tid = int(data.get('id'))
    project_prd = data.get('prd')
    handle_file.write_docs_file(project_prd, "prd", tid)
    # 在这里进行实际的项目创建操作，把requirment.md保存到文件中
    return jsonify({"status": "success", "id": tid, "name": HandleFile.project_id_to_name[tid]}), 200


file_contents = {
    'requirement.md': 'This is the content of requirement.md',
    'system_design.md': 'This is the content of system_design.md',
    'task.md': 'This is the content of task.md'
}

# 模拟的文件生成队列
generated_files = []


# filename的值为requirement、system_design、task、detail
@app.route('/api/generate_docs', methods=['POST'])
def generate_docs():
    data = request.get_json()
    tid = int(data.get('id'))
    filename = data.get('filename')
    if filename in ['requirement', 'system_design', 'detail', 'task']:
        handle_file.generate_docx(filename, tid)
        content = handle_file.get_docs_by_classification(filename, tid)
        generated_files.append(filename+".md")
    # if filename not in generated_files:
    #     generated_files.append(filename)
    #     time.sleep(5)  # simulate file generation delay
        return jsonify({
            "generated": True,
            "fileName": filename,
            "content": content,
            "id": tid, 
            "name": HandleFile.project_id_to_name[tid]
        })
    else:
        return jsonify({"generated": False}), 500


@app.route('/api/generate_code', methods=['POST'])
def generate_code():
    data = request.get_json()
    tid = int(data.get('id'))
    handle_file.generate_code(tid)
    return jsonify({"generated": True, "id": tid, "name": HandleFile.project_id_to_name[tid]}), 200


# 返回文件的文件树
@app.route('/api/get_file_list', methods=['POST'])
def get_file_list():
    data = request.get_json()
    tid = int(data.get('id'))
    filetree = handle_file.get_filetree_by_id(tid)
    # print(filetree)
    return jsonify(filetree), 200


# 参数filename只传递文件名，不传递文件路径和文件后缀
@app.route('/api/get_file_content', methods=['POST'])
def get_file_content():
    data = request.get_json()
    tid = int(data.get('id'))
    filename = data.get('filename')
    if filename in ['prd', 'requirement', 'system_design', 'task', 'detail']:
        content = handle_file.get_docs_by_classification(filename, tid)
    else:
        content = handle_file.get_code_by_filename(filename, tid)
    # 返回文件内容
    return jsonify({"content": content, "id": tid, "name": HandleFile.project_id_to_name[tid]},)


# 更改文件中的内容
@app.route('/api/save_file', methods=['POST'])
def save_file():
    data = request.get_json()
    tid = int(data.get('id'))
    filename = data.get('filename')
    new_content = data.get('content')
    # 保存修改后文件
    if filename in ['prd', 'requirement', 'system_design', 'task', 'detail']:
        handle_file.write_docs_file(new_content, filename, tid)
    else:
        handle_file.write_code_file(new_content, filename, tid)
    return jsonify({"status": "success", "id": tid, "name": HandleFile.project_id_to_name[tid]}), 200


# 未测
# 根据message的建议修改docs类文件的内容，只能为'prd'、'requirement'、'system_design'
@app.route('/api/send_chat_docs', methods=['POST'])
def send_chat():
    data = request.get_json()
    tid = int(data.get('id'))
    filename = data.get('filename')
    message = data.get('message')
    # 根据用户反馈修改文件
    handle_file.rewrite_file(message, filename, tid)
    new_content = ""
    if filename in ['prd', 'requirement', 'system_design', 'task', 'detail']:  
        new_content = handle_file.get_docs_by_classification(filename, tid)
    else:
        new_content = handle_file.get_code_by_filename(filename, tid)
    return jsonify({"new_content": new_content, "id": tid, "name": HandleFile.project_id_to_name[tid]}), 200


# 存在问题，压缩包里内容不对
@app.route('/api/download_files', methods=['POST'])
def download_files():
    tid = int(request.get_json().get('id'))
    print('###', HandleFile.project_id_path[tid])
    # 返回压缩文件
    zip = zipfile.ZipFile("files.zip", 'w', zipfile.ZIP_DEFLATED)
    dirpath = handle_file.project_id_path[tid]
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()    
    return redirect('/files.zip'), 200


@app.route('/api/update_project_name', methods=['POST'])
def update_project_name():
    data = request.get_json()
    tid = int(data.get('id'))
    new_name = data.get('new_name')
    update_name(tid, new_name)
    return jsonify({"status": "success", "id": tid, "name": HandleFile.project_id_to_name[tid]}), 200


@app.route('/api/delete_project_by_id', methods=['POST'])
def delete_project_by_id():
    data = request.get_json()
    tid = int(data.get('id'))
    delete_project(tid)
    return jsonify({"status": "success"}), 200


@app.route('/api/recover_project_by_id', methods=['POST'])
def recover_project_by_id():
    data = request.get_json()
    tid = int(data.get('id'))
    recover_project(tid)
    return jsonify({"status": "success"}), 200


@app.route('/api/show_trash', methods=['GET'])
def show_trash():
    trash = HandleFile.trash
    res = []
    for i in trash.keys():
        res.append({"id": i, "name": trash[i]})
    return jsonify(res), 200


if __name__ == '__main__':
    handle_file = HandleFile()
    app.run(debug=True)
