import json

def lambda_handler(event, context):
    message = {
        "message": "黒飴は奈良中央センターに到着しました！（Hello from Lambda!）"
    }
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": json.dumps(message, ensure_ascii=False)
    }
