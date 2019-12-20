import boto3
import os


def calculate_range_parameter(part_size, part_index, num_parts,
                              total_size=None):
    start_range = part_index * part_size
    if part_index == num_parts - 1:
        end_range = ''
        if total_size is not None:
            end_range = str(total_size - 1)
    else:
        end_range = start_range + part_size - 1
    range_param = 'bytes=%s-%s' % (start_range, end_range)
    return range_param


class UploadHandler:
    def __init__(self, client, bucket, key, uploadId=None, profile=None):
        if client is not None:
            self.client = client
        elif profile is None:
            self.client = boto3.client('s3')
        else:
            session = boto3.Session(profile_name=profile)
            self.client = session.client('s3')
        self.bucket = bucket
        self.key = key
        self.uploadId = uploadId

    def put_object(self, body):
        return self.client.put_object(Bucket=self.bucket, Key=self.key, Body=body)

    def create_multipart_upload(self):
        response = self.client.create_multipart_upload(Bucket=self.bucket, Key=self.key)
        self.uploadId = response.get('UploadId')

    def upload_part(self, part, part_number):
        buckets = self.client.list_buckets()
        response = self.client.upload_part(Body=part,
                                           Bucket=self.bucket,
                                           Key=self.key,
                                           UploadId=self.uploadId,
                                           PartNumber=part_number)
        return dict(ETag=response.get("ETag"), PartNumber=part_number)

    def complete_upload(self, partList):
        self.client.complete_multipart_upload(Bucket=self.bucket,
                                              Key=self.key,
                                              MultipartUpload=dict(Parts=partList),
                                              UploadId=self.uploadId)


class DownloadHandler:
    def __init__(self, bucket, key, profile=None):
        if profile is None:
            myregion = os.environ['region_name']
            self.client = boto3.client('s3', region_name=myregion)
        else:
            session = boto3.Session(profile_name=profile)
            self.client = session.client('s3')
        self.bucket = bucket
        self.key = key

    def download_range(self, range):
        obj = self.client.get_object(Bucket=self.bucket, Key=self.key, Range=range)
        return self.client.get_object(Bucket=self.bucket, Key=self.key, Range=range)

    def download(self):
        return self.client.get_object(Bucket=self.bucket, Key=self.key)

    def get_meta(self):
        resp = self.client.head_object(Bucket=self.bucket, Key=self.key)
        return resp

