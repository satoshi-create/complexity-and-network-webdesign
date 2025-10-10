#!/bin/bash
# ============================================
# 「寸劇で学ぶクラウド」UseCase 05: データ分析
# AWS Textract → S3 → Glue → Athena → QuickSight ハンズオン簡易版
# ============================================

# Step 1. 環境準備 ================================================
# IAMロール作成：LambdaからS3・Textractを操作できる権限を付与
aws iam create-role   --role-name LambdaTextractRole   --assume-role-policy-document file://trust-policy.json

# 必要なポリシーをロールにアタッチ
aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/AmazonTextractFullAccess
aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# IAM設定確認
aws iam get-role --role-name LambdaTextractRole

# Step 2. S3バケット作成とレシートアップロード ====================
# OCR対象のレシートを保存するS3バケットを作成
aws s3 mb s3://oshikatsu-receipts-sg-bucket
aws s3 ls

# サンプル画像アップロード（ローカルの receipt01.jpg）
aws s3 cp ./receipt01.jpg s3://oshikatsu-receipts-sg-bucket/
aws s3 ls s3://oshikatsu-receipts-sg-bucket/

# Step 3. Lambda関数の作成（Textract呼び出し用） =================
# Python関数をZIP化（Windows PowerShellの場合）
powershell Compress-Archive -Path lambda_function.py -DestinationPath function.zip

# Lambda関数作成
aws lambda create-function   --function-name ReceiptOCR   --runtime python3.12   --role arn:aws:iam::<アカウントID>:role/LambdaTextractRole   --handler lambda_function.lambda_handler   --zip-file fileb://function.zip

# 作成確認
aws lambda get-function --function-name ReceiptOCR

# 手動テスト呼び出し
aws lambda invoke   --function-name ReceiptOCR   --payload '{"Records":[{"s3":{"bucket":{"name":"oshikatsu-receipts-sg-bucket"},"object":{"key":"receipt01.jpg"}}}]}'   response.json

# Step 4. S3イベントトリガーの設定 ================================
# 4-1. LambdaにS3トリガー権限を付与
aws lambda add-permission   --function-name ReceiptOCR   --principal s3.amazonaws.com   --statement-id s3invoke   --action "lambda:InvokeFunction"   --source-arn arn:aws:s3:::oshikatsu-receipts-sg-bucket

# 4-2. S3イベント設定：アップロードでLambda自動実行
aws s3api put-bucket-notification-configuration   --bucket oshikatsu-receipts-sg-bucket   --notification-configuration '{
    "LambdaFunctionConfigurations": [
      {
        "LambdaFunctionArn": "arn:aws:lambda:ap-northeast-1:<アカウントID>:function:ReceiptOCR",
        "Events": ["s3:ObjectCreated:*"]
      }
    ]
  }'

# 4-3. 動作確認：新しい画像をアップロード
aws s3 cp receipt02.jpg s3://oshikatsu-receipts-sg-bucket/

# Lambda手動再テスト（必要に応じて）
aws lambda invoke   --function-name ReceiptOCR   --cli-binary-format raw-in-base64-out   --payload '{"Records":[{"s3":{"bucket":{"name":"oshikatsu-receipts-sg-bucket"},"object":{"key":"receipt02.jpg"}}}]}'   response.json

# Step 5. Textract OCRの直接呼び出し（任意テスト） ================
# Textractの直接呼び出しも可能（リージョン指定必須）
aws textract detect-document-text   --document '{"S3Object":{"Bucket":"oshikatsu-receipts-sg-bucket","Name":"receipt02.jpg"}}'   --region ap-northeast-1   > result.json

# Step 6. Glue Crawlerでスキーマ検出 ==============================
# OCR結果（JSON）をS3にアップロード
aws s3 cp ./result.json s3://oshikatsu-receipts-sg-bucket/textract-results/result_openai.json

# JSON整形（1行1オブジェクト形式）
jq -c . result.json > result_line.json
aws s3 cp result_line.json s3://oshikatsu-receipts-sg-bucket/textract-results/

# Glue Crawler作成（AWSコンソールでGUI操作可）
# データベース名: textract_analysis_db
# 対象データ: s3://oshikatsu-receipts-sg-bucket/textract-results/

# Step 7. Athenaクエリ実行 =======================================
# AthenaでOCR結果をSQLで確認
# （AthenaコンソールまたはAWS CLIで実行）
cat << 'EOF'
CREATE EXTERNAL TABLE IF NOT EXISTS textract_analysis_db.receipt_summary_unique (
  BlockType string,      -- Textractのブロック種別（PAGE / LINE / WORDなど）
  Text string,           -- 認識されたテキスト内容
  Confidence double      -- 認識の信頼度（0〜100の実数）
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://oshikatsu-receipts-sg-bucket/structured/'
TBLPROPERTIES ('has_encrypted_data'='false');
EOF

cat << 'EOF'
SELECT BlockType, COUNT(*) AS cnt
FROM textract_analysis_db.receipt_summary_unique
GROUP BY BlockType
LIMIT 10;
EOF

# Step 8. QuickSightで可視化 ======================================
# Athenaのクエリ結果をQuickSightに接続し、ダッシュボード作成

# Step 9. note/ZINEへのまとめ =====================================
# QuickSightダッシュボードをスクリーンショットしてnote投稿
