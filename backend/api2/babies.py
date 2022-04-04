import json
import sys


def lambda_handler(event, context):
    print(event)

    print("paths...")
    for p in sys.path: print(p)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "babies hello world"
        }),
    }
