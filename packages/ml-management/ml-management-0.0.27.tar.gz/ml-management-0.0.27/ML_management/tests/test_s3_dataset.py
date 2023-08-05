import os
import shutil
import unittest
from unittest.mock import Mock, patch

import boto3
import ML_management.dataset.s3_dataset.S3Dataset
from botocore.exceptions import ClientError
from ML_management.dataset.s3_dataset.S3Dataset import S3BucketNotFound, S3FolderNotFound, S3ObjectNotFound


def mock_client_download_successful(*args, **kwargs):
    client = Mock(spec=boto3.client)

    def mock_download_file(Bucket, Key, Filename, ExtraArgs=None, Callback=None, Config=None):
        files_content_map = {
            "sample_data/1.txt": "one\n",
            "sample_data/2.txt": "two\n",
            "sample_data/sample_folder/3.txt": "three\n",
        }
        with open(Filename, "w") as f:
            f.write(files_content_map[Key])

    client.download_file = Mock(side_effect=mock_download_file)
    return client


def mock_client_download_folder_successful(*args, **kwargs):
    client = Mock(spec=boto3.client)

    class mock_paginator:
        def paginate(self, *args, **kwargs):
            return [
                {
                    "KeyCount": 3,
                    "Contents": [
                        {"Key": "sample_data/1.txt"},
                        {"Key": "sample_data/2.txt"},
                        {"Key": "sample_data/sample_folder/3.txt"},
                    ],
                }
            ]

    def mock_download_file(Bucket, Key, Filename, ExtraArgs=None, Callback=None, Config=None):
        files_content_map = {
            "sample_data/1.txt": "one\n",
            "sample_data/2.txt": "two\n",
            "sample_data/sample_folder/3.txt": "three\n",
        }
        with open(Filename, "w") as f:
            f.write(files_content_map[Key])

    client.download_file = Mock(side_effect=mock_download_file)
    client.get_paginator = Mock(return_value=mock_paginator())
    return client


def mock_client_bad_folder(*args, **kwargs):
    client = Mock(spec=boto3.client)

    class mock_paginator:
        def paginate(self, *args, **kwargs):
            return [{"KeyCount": 0}]

    client.get_paginator = Mock(return_value=mock_paginator())
    return client


def mock_client_bad_object(*args, **kwargs):
    client = Mock(spec=boto3.client)

    class mock_paginator:
        def paginate(self, *args, **kwargs):
            return [{"KeyCount": 0}]

    client.download_file = Mock(side_effect=ClientError({"Error": {"Code": "404"}}, "download_file"))
    client.get_paginator = Mock(return_value=mock_paginator())
    client.head_bucket = Mock()
    return client


def mock_client_bad_bucket_folder(*args, **kwargs):
    client = Mock(spec=boto3.client)

    class mock_paginator:
        def paginate(self, *args, **kwargs):
            raise ClientError({"Error": {"Code": "NoSuchBucket"}}, "list_objects_v2")

    client.get_paginator = Mock(return_value=mock_paginator())

    return client


def mock_client_bad_bucket_object(*args, **kwargs):
    client = Mock(spec=boto3.client)

    class mock_paginator:
        def paginate(self, *args, **kwargs):
            return [{"KeyCount": 0}]

    client.download_file = Mock(side_effect=ClientError({"Error": {"Code": "404"}}, "download_file"))
    client.get_paginator = Mock(return_value=mock_paginator())
    client.head_bucket = Mock(side_effect=ClientError({"Error": {"Code": "404"}}, "download_file"))
    return client


class TestS3Dataset(unittest.TestCase):
    """
    Mock S3 structure:

    test-data:
        sample_data/1.txt ("one\n"),
        sample_data/2.txt ("two\n"),
        sample_data/sample_folder/3.txt ("three\n")
    """

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_download_successful,
    )
    def test_download_files(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_download_successful is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        local_path = s3_dataset.set_data(
            local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
            bucket="test-data",
            remote_paths=[
                "sample_data/1.txt",
                "sample_data/2.txt",
                "sample_data/sample_folder/3.txt",
            ],
            endpoint_url=endpoint_url,
            aws_access_key_id="some_mock_key",
            aws_secret_access_key="some_mock_key",
        )

        with open(os.path.join(local_path, "sample_data/1.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "one\n")
        with open(os.path.join(local_path, "sample_data/2.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "two\n")
        with open(os.path.join(local_path, "sample_data/sample_folder/3.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "three\n")

        shutil.rmtree(os.path.join(local_path, "sample_data/"))

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_download_folder_successful,
    )
    def test_download_folder(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_download_folder_successful is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        local_path = s3_dataset.set_data(
            local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
            bucket="test-data",
            remote_paths=["sample_data/"],
            endpoint_url=endpoint_url,
            aws_access_key_id="some_mock_key",
            aws_secret_access_key="some_mock_key",
        )

        with open(os.path.join(local_path, "sample_data/1.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "one\n")
        with open(os.path.join(local_path, "sample_data/2.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "two\n")
        with open(os.path.join(local_path, "sample_data/sample_folder/3.txt"), "r") as f:
            text_one = f.read()
            self.assertEqual(text_one, "three\n")

        shutil.rmtree(os.path.join(local_path, "sample_data/"))

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_bad_object,
    )
    def test_download_bad_object(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_bad_object is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        with self.assertRaises(S3ObjectNotFound):
            s3_dataset.set_data(
                local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
                bucket="test-data",
                remote_paths=["sample_data/nosuchfile.txt"],
                endpoint_url=endpoint_url,
                aws_access_key_id="some_mock_key",
                aws_secret_access_key="some_mock_key",
            )

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_bad_folder,
    )
    def test_download_bad_folder(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_bad_folder is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        with self.assertRaises(S3FolderNotFound):
            s3_dataset.set_data(
                local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
                bucket="test-data",
                remote_paths=["sample_data/nosuchfolder/"],
                endpoint_url=endpoint_url,
                aws_access_key_id="some_mock_key",
                aws_secret_access_key="some_mock_key",
            )

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_bad_bucket_folder,
    )
    def test_download_bad_bucket_folder(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_bad_bucket_folder is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        with self.assertRaises(S3BucketNotFound):
            s3_dataset.set_data(
                local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
                bucket="nosuchbucket",
                remote_paths=["sample_data/"],
                endpoint_url=endpoint_url,
                aws_access_key_id="some_mock_key",
                aws_secret_access_key="some_mock_key",
            )

    @patch(
        "ML_management.dataset.s3_dataset.S3Dataset.client",
        new=mock_client_bad_bucket_object,
    )
    def test_download_bad_bucket_object(self):
        s3_dataset = ML_management.dataset.s3_dataset.S3Dataset.S3Dataset()
        assert mock_client_bad_bucket_object is ML_management.dataset.s3_dataset.S3Dataset.client
        endpoint_url = "some_mock_url"

        with self.assertRaises(S3BucketNotFound):
            s3_dataset.set_data(
                local_path=os.path.join(os.path.dirname(__file__), "downloaded_data/"),
                bucket="nosuchbucket",
                remote_paths=["sample_data/1.txt"],
                endpoint_url=endpoint_url,
                aws_access_key_id="some_mock_key",
                aws_secret_access_key="some_mock_key",
            )


if __name__ == "__main__":
    unittest.main()
