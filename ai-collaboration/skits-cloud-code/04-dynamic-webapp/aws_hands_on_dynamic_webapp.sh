#!/bin/bash
# =========================================================
# 📘 AWSハンズオン：UseCase 04 - 動的Webアプリ
# クラウド三部作（DynamoDB / Lambda / API Gateway）＋ S3＋CloudFront
# =========================================================

# =========================================================
# Step 1️⃣ 書記官 DynamoDB：テーブル作成
# =========================================================

aws dynamodb create-table   --table-name RideOrders   --attribute-definitions AttributeName=orderId,AttributeType=S   --key-schema AttributeName=orderId,KeyType=HASH   --billing-mode PAY_PER_REQUEST

aws dynamodb list-tables

aws dynamodb put-item   --table-name RideOrders   --item file://item.json

# =========================================================
# Step 2️⃣ 一芸役者 Lambda：関数作成
# =========================================================

zip function.zip lambda_function.py

aws lambda create-function   --function-name handleRideRequest   --zip-file fileb://function.zip   --handler lambda_function.lambda_handler   --runtime python3.12   --role arn:aws:iam::<アカウントID>:role/lambda-ex-role

aws lambda update-function-code   --function-name handleRideRequest   --zip-file fileb://function.zip

# =========================================================
# Step 3️⃣ 親分の許可証：Lambdaに実行ロール付与（DynamoDBアクセス）
# =========================================================

aws iam create-role   --role-name lambda-dynamodb-access-role   --assume-role-policy-document file://trust-policy.json

aws iam attach-role-policy   --role-name lambda-ex-role   --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam attach-role-policy   --role-name lambda-ex-role   --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess

# =========================================================
# Step 4️⃣ 門番 API Gateway：Lambdaと統合
# =========================================================

aws apigateway create-rest-api --name "RideOrderAPI"

aws apigateway get-resources --rest-api-id <api_id>

aws apigateway create-resource   --rest-api-id <api_id>   --parent-id <root_id>   --path-part ride

aws apigateway put-method   --rest-api-id <api_id>   --resource-id <resource_id>   --http-method POST   --authorization-type "NONE"

aws lambda get-function   --function-name handleRideRequest   --query "Configuration.FunctionArn" --output text

aws apigateway put-integration   --rest-api-id <api_id>   --resource-id <resource_id>   --http-method POST   --type AWS_PROXY   --integration-http-method POST   --uri arn:aws:apigateway:ap-northeast-1:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-northeast-1:<アカウントID>:function:handleRideRequest/invocations

aws lambda add-permission   --function-name handleRideRequest   --statement-id apigateway-access   --action lambda:InvokeFunction   --principal apigateway.amazonaws.com   --source-arn arn:aws:execute-api:ap-northeast-1:<アカウントID>:<api_id>/*/POST/ride

# =========================================================
# Step 5️⃣ 舞台公開：APIをデプロイ
# =========================================================

aws apigateway create-deployment   --rest-api-id <api_id>   --stage-name prod

curl -X POST "https://<api_id>.execute-api.ap-northeast-1.amazonaws.com/prod/ride"

# =========================================================
# Step 6️⃣ カタカナ大臣＋フロントちゃん：フロントエンド作成
# =========================================================

# index.html内でfetch関数を設定
# fetch("https://<api_id>.execute-api.ap-northeast-1.amazonaws.com/prod/ride", { method: "POST" })
#   .then(res => res.json())
#   .then(data => console.log(data));

# =========================================================
# Step 7️⃣ ブラウザとクラウドの共演：CORS設定
# =========================================================

# Lambdaのレスポンスに以下を追加
# "headers": {
#   "Access-Control-Allow-Origin": "*",
#   "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
#   "Access-Control-Allow-Headers": "Content-Type"
# }

# =========================================================
# Step 8️⃣ ゴジュエモン登場：CloudWatchログ確認
# =========================================================

aws logs describe-log-groups

aws logs describe-log-streams   --log-group-name "/aws/lambda/handleRideRequest"   --order-by LastEventTime   --descending --max-items 3

aws logs get-log-events   --log-group-name "/aws/lambda/handleRideRequest"   --log-stream-name "<latest_stream_name>"   --limit 20

# =========================================================
# 🎬 Appendix：CloudFront + S3 公開版（UseCase 04 拡張）
# =========================================================

aws cloudfront create-distribution   --origin-domain-name ride-app-web.s3-website-ap-northeast-1.amazonaws.com   --default-root-object index.html

aws cloudfront get-distribution   --id <distribution_id>   --query "Distribution.Status"

aws s3api put-public-access-block   --bucket ride-app-web   --public-access-block-configuration '{
      "BlockPublicAcls": true,
      "IgnorePublicAcls": true,
      "BlockPublicPolicy": true,
      "RestrictPublicBuckets": true
  }'
