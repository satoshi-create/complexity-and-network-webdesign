#!/bin/bash

# UseCase 03: Serverless API (AWS Lambda + API Gateway 編, MVP)
# Lambda関数の作成からAPI Gateway統合、エンドポイント公開まで

# 1. Lambda関数をZIP化
zip -r function.zip lambda_function.py

# 2. IAMロール作成（Lambda実行用）
cat > trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "lambda.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

aws iam create-role \
  --role-name lambda-ex-role \
  --assume-role-policy-document file://trust-policy.json

# Lambda実行ロールにCloudWatchログ出力権限を付与
aws iam attach-role-policy \
  --role-name lambda-ex-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# 3. Lambda関数作成
ROLE_ARN=$(aws iam get-role --role-name lambda-ex-role --query 'Role.Arn' --output text)

aws lambda create-function \
  --function-name hello-nara-api \
  --runtime python3.9 \
  --role $ROLE_ARN \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip

# 4. API Gateway 作成
API_ID=$(aws apigateway create-rest-api \
  --name "NaraDeliveryAPI" \
  --query 'id' --output text)

# 5. ルートリソースID取得
ROOT_ID=$(aws apigateway get-resources \
  --rest-api-id $API_ID \
  --query 'items[?path==`"/"`].id' --output text)

# 6. /status リソース作成
RESOURCE_ID=$(aws apigateway create-resource \
  --rest-api-id $API_ID \
  --parent-id $ROOT_ID \
  --path-part status \
  --query 'id' --output text)

# 7. GETメソッド作成
aws apigateway put-method \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method GET \
  --authorization-type "NONE"

# 8. Lambda統合設定
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

aws apigateway put-integration \
  --rest-api-id $API_ID \
  --resource-id $RESOURCE_ID \
  --http-method GET \
  --type AWS_PROXY \
  --integration-http-method POST \
  --uri arn:aws:apigateway:ap-northeast-1:lambda:path/2015-03-31/functions/arn:aws:lambda:ap-northeast-1:$ACCOUNT_ID:function:hello-nara-api/invocations

# 9. API Gateway に Lambda 実行権限を付与
aws lambda add-permission \
  --function-name hello-nara-api \
  --statement-id apigateway-permission \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn arn:aws:execute-api:ap-northeast-1:$ACCOUNT_ID:$API_ID/*/GET/status

# 10. API デプロイ（ステージ名: dev）
aws apigateway create-deployment \
  --rest-api-id $API_ID \
  --stage-name dev

# 11. エンドポイントURLを出力
echo "✅ APIエンドポイント:"
echo "https://$API_ID.execute-api.ap-northeast-1.amazonaws.com/dev/status"
