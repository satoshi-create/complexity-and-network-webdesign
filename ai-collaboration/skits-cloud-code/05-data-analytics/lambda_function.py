# ============================================
# lambda_function.py
# AWS Lambda 関数：S3にアップロードされたレシート画像をTextractでOCR処理し、
# 結果(JSON)を同じS3バケットに保存する。
# ============================================

import boto3
import json

# Textractクライアントの初期化
# ※リージョンはバケットに合わせて指定（例: ap-southeast-1）
textract = boto3.client('textract', region_name='ap-southeast-1')

# S3クライアントの初期化
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambdaエントリポイント。
    S3に画像がアップロードされたイベントを受け取り、
    Textractを呼び出してOCR結果をS3に保存する。
    """
    for record in event['Records']:
        # OCR対象のS3バケット名（固定化する場合はここで設定）
        bucket = "oshikatsu-receipts-sg-bucket"
        # アップロードされたファイル名を取得
        key = record['s3']['object']['key']

        # TextractによるOCR（テキスト検出API）
        response = textract.detect_document_text(
            Document={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key
                }
            }
        )

        # 出力ファイル名を定義（.jpg → _extracted.json）
        result_key = key.replace('.jpg', '_extracted.json')

        # OCR結果(JSON)をS3に保存
        s3.put_object(
            Bucket=bucket,
            Key=result_key,
            Body=json.dumps(response, ensure_ascii=False)
        )

        # CloudWatch Logs で確認用出力（任意）
        print(f"OCR完了: {key} → {result_key}")
