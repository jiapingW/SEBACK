from manager import Manager

manager = Manager()


def start_project_from_idea(idea: str):
    code = manager.start_project(idea)
    print(code)


def start_project_from_engineer():
    code = manager.start_project_from_engineer()
    print(code)









