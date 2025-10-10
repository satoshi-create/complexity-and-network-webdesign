# ☁️ UseCase 05: データ分析（Data Analytics）

Textract → S3 → Glue → Athena → QuickSight まで、データがクラウドで“語り始める”旅。

---

## 📘 目次

- [Step 0️⃣ 環境準備（IAM と CLI 設定）](#step-0️⃣-環境準備iam-と-cli-設定)
- [Step 1️⃣ S3 バケット作成とレシートアップロード](#step-1️⃣-s3-バケット作成とレシートアップロード)
- [Step 2️⃣ Lambda 関数の作成（Textract 呼び出し用）](#step-2️⃣-lambda-関数の作成textract-呼び出し用)
- [Step 3️⃣ S3 イベントトリガーの設定](#step-3️⃣-s3-イベントトリガーの設定)
- [Step 4️⃣ Textract OCR 実行と結果確認](#step-4️⃣-textract-ocr-実行と結果確認)
- [Step 5️⃣ Glue Crawler でスキーマ検出](#step-5️⃣-glue-crawler-でスキーマ検出)
- [Step 6️⃣ Athena で SQL クエリ実行](#step-6️⃣-athena-で-sql-クエリ実行)
- [Step 7️⃣ QuickSight で可視化](#step-7️⃣-quicksight-で可視化)
- [Step 8️⃣ note まとめ](#step-8️⃣-note-まとめ)

---

## Step 0️⃣ 環境準備（IAM と CLI 設定）

AWS CLI が利用できることを確認します。

```bash
aws configure
```

IAM ロールを作成し、Lambda が S3 と Textract にアクセスできるよう設定します。

```bash
aws iam create-role   --role-name LambdaTextractRole   --assume-role-policy-document file://trust-policy.json

aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/AmazonTextractFullAccess
aws iam attach-role-policy --role-name LambdaTextractRole --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

---

## Step 1️⃣ S3 バケット作成とレシートアップロード

OCR 対象データ（レシート）を保存する S3 バケットを作成し、画像をアップロードします。

```bash
aws s3 mb s3://oshikatsu-receipts-sg-bucket
aws s3 cp ./receipt01.jpg s3://oshikatsu-receipts-sg-bucket/
aws s3 ls s3://oshikatsu-receipts-sg-bucket/
```

> ✅ S3 はすべてのデータが集まる「中継地点」。以降の処理はここを起点に動作します。

---

## Step 2️⃣ Lambda 関数の作成（Textract 呼び出し用）

Python 関数を ZIP 化し、Lambda 関数を作成します。

```bash
powershell Compress-Archive -Path lambda_function.py -DestinationPath function.zip

aws lambda create-function   --function-name ReceiptOCR   --runtime python3.12   --role arn:aws:iam::<アカウントID>:role/LambdaTextractRole   --handler lambda_function.lambda_handler   --zip-file fileb://function.zip
```

関数コード例：

```python
import boto3, json

def lambda_handler(event, context):
    textract = boto3.client('textract')
    s3 = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        response = textract.detect_document_text(
            Document={'S3Object': {'Bucket': bucket, 'Name': key}}
        )
        s3.put_object(
            Bucket=bucket,
            Key=f"textract-results/{key.replace('.jpg','.json')}",
            Body=json.dumps(response)
        )
```

---

## Step 3️⃣ S3 イベントトリガーの設定

S3 にファイルがアップロードされたとき、自動的に Lambda を呼び出す設定を追加します。

```bash
aws lambda add-permission   --function-name ReceiptOCR   --principal s3.amazonaws.com   --statement-id s3invoke   --action "lambda:InvokeFunction"   --source-arn arn:aws:s3:::oshikatsu-receipts-sg-bucket

aws s3api put-bucket-notification-configuration   --bucket oshikatsu-receipts-sg-bucket   --notification-configuration '{
    "LambdaFunctionConfigurations": [
      {
        "LambdaFunctionArn": "arn:aws:lambda:ap-northeast-1:<アカウントID>:function:ReceiptOCR",
        "Events": ["s3:ObjectCreated:*"]
      }
    ]
  }'
```

📡 **テスト：**

```bash
aws s3 cp receipt02.jpg s3://oshikatsu-receipts-sg-bucket/
```

> Lambda ログを CloudWatch で確認し、Textract 処理が発火していれば成功。

---

## Step 4️⃣ Textract OCR 実行と結果確認

Lambda 経由で自動処理されるほか、手動で Textract API を呼び出すことも可能です。

```bash
aws textract detect-document-text   --document '{"S3Object":{"Bucket":"oshikatsu-receipts-sg-bucket","Name":"receipt02.jpg"}}'   --region ap-northeast-1   > result.json
```

生成された `result.json` は、次の Glue ステップで解析されます。

---

## Step 5️⃣ Glue Crawler でスキーマ検出

1. Glue コンソールで新しい **Crawler** を作成
2. データソース：`s3://oshikatsu-receipts-sg-bucket/textract-results/`
3. 出力：Data Catalog → データベース名 `textract_analysis_db`
4. 実行後、Athena で `receipt_ndjson` テーブルが確認できれば成功。

---

## Step 6️⃣ Athena で SQL クエリ実行

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS textract_analysis_db.receipt_ndjson (
  BlockType string,
  Text string,
  Confidence double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://oshikatsu-receipts-sg-bucket/textract-results/'
TBLPROPERTIES ('has_encrypted_data'='false');

SELECT BlockType, COUNT(*) AS cnt
FROM textract_analysis_db.receipt_ndjson
GROUP BY BlockType
LIMIT 10;
```

> 🎯 目的：Textract OCR 結果(JSON)を構造化データとして SQL で分析可能にする。

---

## Step 7️⃣ QuickSight で可視化

Athena クエリ結果を QuickSight に接続し、以下のようなグラフを作成します。

- 棒グラフ：OCR 認識カテゴリ別件数
- 円グラフ：支出カテゴリ比率
- 折れ線／ヒートマップ：Confidence スコア分布

> 💡 QuickSight は、クラウドが「自分のデータを見つめる鏡」。
