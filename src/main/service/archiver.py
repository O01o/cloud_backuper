from src.main.repository.storage.interface.archiver import Archiver

_archiver: Archiver | None = None

def init_archiver(archiver: Archiver):
    global _archiver
    _archiver = archiver

def archive(local_path: str, upload_path: str, encryption: bool):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.archive(
        local_path=local_path,
        upload_path=upload_path,
        encryption=encryption,
    )

def push_tree(local_path: str, upload_path: str):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.push_tree(
        local_path=local_path,
        upload_path=upload_path,
    )

def restore(local_path: str, upload_path: str):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.restore(
        local_path=local_path,
        upload_path=upload_path,
    )
