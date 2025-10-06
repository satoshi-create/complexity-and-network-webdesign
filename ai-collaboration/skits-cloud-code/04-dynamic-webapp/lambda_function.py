import json
import boto3
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RideOrders')  # ←テーブル名確認

def lambda_handler(event, context):
    print("📩 受信イベント:", json.dumps(event))
    try:
        order_id = str(random.randint(1, 999)).zfill(3)
        driver = "ゴジュエモンタクシー"
        eta = "3分後"

        table.put_item(
            Item={
                "orderId": order_id,
                "driverName": driver,
                "eta": eta,
                "status": "on_the_way"
            }
        )
        print(f"✅ DynamoDB 登録成功: {order_id}")

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
             },
            "body": json.dumps({
                "orderId": order_id,
                "driverName": driver,
                "eta": eta
            })
        }

    except Exception as e:
        print(f"💥 エラー発生: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
