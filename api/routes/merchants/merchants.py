import json
import boto3
import sys

from controllers.MerchantsController import GetMerchants
from helpers import validate_login_token

def lambda_handler(event, context):
    print(event)
    print("\n")

    print("boto3 version: ", boto3.__version__)

    print("Validate login Token...")
    res = validate_login_token()
    print(str(res))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello from merchants",
            "data": GetMerchants()
        }),
    }
