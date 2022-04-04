import json


def lambda_handler(event, context):
    print(event)
    print("\n")


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello from logs_event"
        }),
    }
