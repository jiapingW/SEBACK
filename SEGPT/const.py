from pathlib import Path
import shutil


def get_project_root():
    """逐级向上寻找项目根目录"""
    current_path = Path.cwd()
    while True:
        if (current_path / '.git').exists() or \
           (current_path / '.project_root').exists() or \
           (current_path / '.gitignore').exists():
            return current_path
        parent_path = current_path.parent
        if parent_path == current_path:
            raise Exception("Project root not found.")
        current_path = parent_path


def recreate_workspace(workspace: Path):
    try:
        shutil.rmtree(workspace)
    except FileNotFoundError:
        pass  # 文件夹不存在，但我们不在意
    workspace.mkdir(parents=True, exist_ok=True)


PROJECT_ROOT = get_project_root()
DATA_PATH = PROJECT_ROOT / 'data'
WORKSPACE_ROOT = PROJECT_ROOT / 'workspace'
PROMPT_PATH = PROJECT_ROOT / 'segpt/prompts'
UT_PATH = PROJECT_ROOT / 'data/ut'
SWAGGER_PATH = UT_PATH / "files/api/"
UT_PY_PATH = UT_PATH / "files/ut/"
API_QUESTIONS_PATH = UT_PATH / "files/question/"
YAPI_URL = "http://yapi.deepwisdomai.com/"
TMP = PROJECT_ROOT / 'tmp'
RESEARCH_PATH = DATA_PATH / "research"

MEM_TTL = 24 * 30 * 3600
