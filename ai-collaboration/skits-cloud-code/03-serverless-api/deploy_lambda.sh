#!/bin/bash
aws lambda create-function \
  --function-name hello-nara-api \
  --runtime python3.9 \
  --role arn:aws:iam::902878533347:role/lambda-ex-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip


aws lambda create-function --function-name hello-nara-api --runtime python3.9  --role arn:aws:iam::902878533347:role/lambda-ex-role --handler lambda_function.lambda_handler --zip-file fileb://function.zip
