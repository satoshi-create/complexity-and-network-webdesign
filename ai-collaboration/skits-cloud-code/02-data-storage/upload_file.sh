#!/bin/bash

# UseCase 02: Data Storage (AWS S3編, MVP)
# S3バケット作成から動画ファイル保存、アクセス確認まで

# 1. S3 バケット作成
aws s3 mb s3://my-idol-video-bucket

# 2. 動画ファイルアップロード
aws s3 cp sample_video.mp4 s3://my-idol-video-bucket/ \
  --content-type "video/mp4"

# 3. バケット内オブジェクト一覧確認
aws s3 ls s3://my-idol-video-bucket/

# 4. presign URL 発行（有効期限: 1時間）
echo "Presign URL (有効期限: 3600秒)"
aws s3 presign s3://my-idol-video-bucket/sample_video.mp4 --expires-in 3600
