import json
import requests
import sys
import base64
import cgi
import io


def lambda_handler(event, context):
    print(event)
    print("\n")
    
    # print("paths...")
    # for p in sys.path: print(p)

    # print(event.get("body"))
    # event_body = json.loads(event.get("body"))
    # print(event_body.get("details"))
    
    f_body = event["body"]
    if event.get("isBase64Encoded"):
        f_body = base64.b64decode(f_body)
        
    fp = io.BytesIO(f_body)
    pdict = cgi.parse_header(event["headers"]["Content-Type"])[1]
    if 'boundary' in pdict:
        pdict['boundary'] = pdict['boundary'].encode('utf-8')
    pdict['CONTENT-LENGTH'] = len(event['body'])
    form_data = cgi.parse_multipart(fp, pdict)
    print("form_data: ", form_data)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
