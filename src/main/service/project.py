from src.main.repository.storage.interface.project import Project

_project: Project | None = None

def init_project(project: Project):
    global _project
    _project = project

def push(origin_path: str, backup_path: str, encryption: bool):
    assert _project is not None, "Project must be initialized"
    _project.push(
        origin_path=origin_path,
        backup_path=backup_path,
        encryption=encryption,
    )

def push_tree(origin_path: str, backup_path: str):
    assert _project is not None, "Project must be initialized"
    _project.push_tree(
        origin_path=origin_path,
        backup_path=backup_path,
    )

def pull(origin_path: str, backup_path: str):
    assert _project is not None, "Project must be initialized"
    _project.pull(
        origin_path=origin_path,
        backup_path=backup_path,
    )