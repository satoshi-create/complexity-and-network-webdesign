# 1. バケット作成（例: my-static-site-202510）
aws s3 mb s3://my-static-site-202510

# 2. index.html をアップロード
aws s3 cp index.html s3://my-static-site-202510/

# 3. バケットをウェブサイト用に設定
aws s3 website s3://my-static-site-202510/ --index-document index.html

# 4. バケットポリシーを追加して公開設定（誰でも閲覧できるようにする）
cat > bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-static-site-202510/*"
    }
  ]
}
EOF

aws s3api put-bucket-policy --bucket my-static-site-202510 --policy file://bucket-policy.json
