from src.main.repository.storage.interface.archiver import Archiver

_archiver: Archiver | None = None

def init_archiver(archiver: Archiver):
    global _archiver
    _archiver = archiver

def archive(origin_path: str, backup_path: str, encryption: bool):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.archive(
        origin_path=origin_path,
        backup_path=backup_path,
        encryption=encryption,
    )

def push_tree(origin_path: str, backup_path: str):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.push_tree(
        origin_path=origin_path,
        backup_path=backup_path,
    )

def restore(origin_path: str, backup_path: str):
    assert _archiver is not None, "Archiver must be initialized"
    _archiver.restore(
        origin_path=origin_path,
        backup_path=backup_path,
    )
