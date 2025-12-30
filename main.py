import os

from src.main.repository.storage.s3 import project_versioner as project_versioner_s3_repository
from src.main.repository.storage.mock import project_versioner as project_versioner_mock_repository
from src.main.repository.storage.s3 import archiver as archiver_s3_repository
from src.main.repository.storage.mock import archiver as archiver_mock_repository

from src.main.service import project_versioner as project_versioner_service
from src.main.service import archiver as archiver_service

local_path: str = os.path.join(".", "src")
upload_path: str = os.path.join(".", "src")

project_versioner_s3_repository.init_bucket(bucket_name="")
# project_versioner_service.init_project_versioner(project_versioner=project_versioner_s3_repository)
project_versioner_service.init_project_versioner(project_versioner=project_versioner_mock_repository)
project_versioner_service.push(
    local_path=local_path,
    upload_path=upload_path,
    encryption=False,
)
print()
project_versioner_service.push_tree(
    local_path=local_path,
    upload_path=upload_path,
)
