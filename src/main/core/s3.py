import boto3

def setup_bucket_lcp(bucket_name: str):
    s3_client = boto3.client('s3')

    s3_client.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"Enabled versioning on bucket: {bucket_name}")

    lifecycle_config = {
        'Rules': [
            {
                'ID': 'MoveToArchiveRule',
                'Filter': {'Prefix': ''},
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 90,
                        'StorageClass': 'GLACIER'
                    }
                ],
                'NoncurrentVersionTransitions': [
                    {
                        'NoncurrentDays': 30,
                        'StorageClass': 'DEEP_ARCHIVE'
                    }
                ],
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 7
                },
            }
        ]
    }

    s3_client.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_config
    )
    print(f"Applied lifecycle policy (Archive after 90 days) to: {bucket_name}")