import boto3;
import json
import os
from time import sleep
from sqs_utils import SQSQueue
import oss2
from s3_utils import UploadHandler
def download_to_local( ):
    while True:
        message_str = task_queue.get_message()
        if message_str is None:
            print('sleep')
            sleep(5)
        else:
            message = json.loads(message_str)
            src_bucket = message['src_bucket']
            dest_bucket=os.environ['destbucket']
            object_name = message['object_name']
            # endpoint=os.environ['endpoint']
            endpoint = ssm_client.get_parameter(Name='endpoint')['Parameter']['Value']
            #accesskey_id=os.environ['ali_accesskey_id']
            #accesskey_secret= os.environ['ali_accesskey_secret']
            accesskey_id = ssm_client.get_parameter(Name='accesskey_id')['Parameter']['Value']
            accesskey_secret = ssm_client.get_parameter(Name='accesskey_secret')['Parameter']['Value']
            auth = oss2.Auth(accesskey_id, accesskey_secret)
            bucket = oss2.Bucket(auth, endpoint, src_bucket);
            object_stream = bucket.get_object(object_name)
            uploader = UploadHandler(bucket=dest_bucket, key=object_name, client=target_client)
            uploader.put_object(object_stream.read())
            print('end')
            task_queue.delete_message()

if __name__ == '__main__':
    china_aws_rg=os.environ['china_aws_rg']
    #aws_key_id=os.environ['aws_key_id']
    #aws_secret_access_key=os.environ['aws_secret_access_key']
    #sqs_name=os.environ['sqs_name']
    target_client = boto3.client('s3',region_name=china_aws_rg)
    ssm_client = boto3.client('ssm',region_name=china_aws_rg)
    sqs_name = ssm_client.get_parameter(Name='sqs_name')['Parameter']['Value']
    download_local_save_prefix = " ";
    task_queue = SQSQueue(None, queue_name=sqs_name)
    print('end')
    download_to_local()
