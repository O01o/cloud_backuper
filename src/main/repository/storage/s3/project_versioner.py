import os
import boto3

from src.main.logic import tree

_s3_client = boto3.client('s3')
_bucket_name: str | None = None

def init_bucket(bucket_name: str):
    global _bucket_name
    _bucket_name = bucket_name

def push(local_path: str, upload_path: str, encryption: bool):
    assert _bucket_name is not None, "bucket_name must be initialized"
    # upload to s3 recursively
    for root, _, files in os.walk(local_path):
        for file_child_path in files:
            # define upload path
            local_edge_path = os.path.join(root, file_child_path)
            upload_edge_path = os.path.join(upload_path, os.path.relpath(local_edge_path, local_path))
            # TODO: encryption option
            # upload to s3
            try:
                _s3_client.upload_file(
                    Filename=local_edge_path,
                    Bucket=_bucket_name,
                    Key=upload_edge_path,
                    ExtraArgs={
                        'StorageClass': 'STANDARD_IA'
                    }
                )
            except Exception as e:
                print(f"Error S3 uploading {local_path} to {upload_path}:", e)

def push_tree(local_path: str, upload_path: str):
    assert _bucket_name is not None, "bucket_name must be initialized"
    try:
        _s3_client.upload_file(
            Filename=tree.get_tree(local_path),
            Bucket=_bucket_name,
            Key=upload_path,
            ExtraArgs={
                'StorageClass': 'STANDARD_IA'
            }
        )
    except Exception as e:
        print(f"Error S3 uploading {local_path} to {upload_path}:", e)

def pull(local_path: str, upload_path: str):
    assert _bucket_name is not None, "bucket_name must be initialized"

