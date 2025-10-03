#!/bin/bash
zip function.zip lambda_function.py
aws lambda create-function --function-name HelloFunction --runtime python3.9 --role <IAM_ROLE_ARN> --handler lambda_function.lambda_handler --zip-file fileb://function.zip
