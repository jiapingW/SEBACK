from flask import Flask, request, send_file
import zipfile
import os
import tempfile

app = Flask(__name__)

@app.route('/api/download_files', methods=['POST'])
def download_files():
    dirpath = request.form.get('dirpath')
    print(dirpath)
    # 检查dirpath是否存在，以及是否是一个目录
    if dirpath is None or not os.path.exists(dirpath) or not os.path.isdir(dirpath):
        return "Invalid or missing 'dirpath'", 400

    # 创建临时ZIP文件
    temp_zip = tempfile.NamedTemporaryFile(delete=False)
    with zipfile.ZipFile(temp_zip.name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(dirpath):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), dirpath))

    return send_file(temp_zip.name,
                     mimetype='application/zip',
                     as_attachment=True,
                     download_name='file.zip',
                     attachment_filename='file.zip')


if __name__ == '__main__':
    app.run(debug=True)