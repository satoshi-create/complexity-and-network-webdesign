#!/bin/bash

# UseCase 01: Static Site デプロイスクリプト
# S3バケット作成からCloudFront配信まで

# 1. S3 バケット作成
aws s3 mb s3://my-first-bucket-202XXXXX

# 2. index.html アップロード
aws s3 cp index.html s3://my-first-bucket-202XXXXX/

# 3. 静的ウェブサイトホスティング有効化
aws s3 website s3://my-first-bucket-202XXXXX/ --index-document index.html

# 4. バケットポリシー適用（公開許可）
aws s3api put-bucket-policy \\
  --bucket my-first-bucket-202XXXXX \\
  --policy file://bucket-policy.json

# 5. 公開URL確認 (S3)
echo "S3 Website URL:"
echo "http://my-first-bucket-202XXXXX.s3-website-ap-northeast-1.amazonaws.com"

# 6. CloudFront ディストリビューション作成
aws cloudfront create-distribution \\
  --origin-domain-name my-first-bucket-202XXXXX.s3.ap-northeast-1.amazonaws.com \\
  --default-root-object index.html > cloudfront.json

# 7. CloudFront URL確認
CLOUDFRONT_DOMAIN=$(jq -r '.Distribution.DomainName' cloudfront.json)
echo "CloudFront URL:"
echo "https://$CLOUDFRONT_DOMAIN/index.html"
