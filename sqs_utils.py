import json
import boto3
import botocore
import logging
import os

class SQSQueue:
    def __init__(self, profile, queue_name, timeout=1800):
        if profile is None:
            #aws_access_key_id =os.environ['aws_key_id']
            #aws_secret_access_key = os.environ['aws_secret_access_key']
            china_aws_rg=os.environ['china_aws_rg']
            self.client = boto3.client('sqs',region_name=china_aws_rg)
            logging.info('error1')
        else:
            logging.info("initial the sqs client with profile %s" % profile)
            session = boto3.Session(profile_name=profile)
            self.client = session.client('sqs')
        try:
            self.url = self.client.get_queue_url(QueueName=queue_name)['QueueUrl']
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "AWS.SimpleQueueService.NonExistentQueue":
                logging.exception("The %s queue can't be found, will be created automatically" % queue_name)
                self.url = self.client.create_queue(
                    QueueName=queue_name,
                    Attributes={
                        'VisibilityTimeout': '%d' % timeout
                    }
                )['QueueUrl']
            else:
                raise e
        self.receipt = None

    def get_message(self):
        resp = self.client.receive_message(
            QueueUrl=self.url,
            MaxNumberOfMessages=1
        )
        if resp.get('Messages', None) is None:
            return None
        self.receipt = resp['Messages'][0]['ReceiptHandle']
        return resp['Messages'][0]['Body']

    def send_message(self, message):
        resp = self.client.send_message(
            QueueUrl=self.url,
            MessageBody=message
        )
        return resp.get('MessageId', None)

    def delete_message(self):
        response = self.client.delete_message(
            QueueUrl=self.url,
            ReceiptHandle=self.receipt
        )


