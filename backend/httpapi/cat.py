import json
import sys
import boto3
import os


def lambda_handler(event, context):
    print(event)

    try:
        print(f"Triggering SNS...")
        sns_client = boto3.client('sns')
        response = sns_client.publish(TopicArn=os.environ.get("sns_logs_arn"), Message="Hello from SNS", Subject="sns.triggered")
        message_id = response['MessageId']
        print(message_id)
    except Exception as e:
        print("SNS ERROR: ", str(e))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello from http api endpoint"
        }),
    }
