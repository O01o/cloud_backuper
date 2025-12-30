from src.main.repository.storage.interface.project_versioner import ProjectVersioner

_project_versioner: ProjectVersioner | None = None

def init_project_versioner(project_versioner: ProjectVersioner):
    global _project_versioner
    _project_versioner = project_versioner

def push(local_path: str, upload_path: str, encryption: bool):
    assert _project_versioner is not None, "Project must be initialized"
    _project_versioner.push(
        local_path=local_path,
        upload_path=upload_path,
        encryption=encryption,
    )

def push_tree(local_path: str, upload_path: str):
    assert _project_versioner is not None, "Project must be initialized"
    _project_versioner.push_tree(
        local_path=local_path,
        upload_path=upload_path,
    )

def pull(local_path: str, upload_path: str):
    assert _project_versioner is not None, "Project must be initialized"
    _project_versioner.pull(
        local_path=local_path,
        upload_path=upload_path,
    )