# データ保存

S3 にデータを保存し、バージョン管理を体験する。

1. **S3 バケット作成**

   ```bash
   aws s3 mb s3://my-idol-video-bucket

   ```

2. **動画ファイルをアップロード**

   ```bash
   aws s3 cp sample_video.mp4 s3://my-idol-video-bucket/ \
     --content-type "video/mp4"

   ```

3. **オブジェクト一覧を確認**

   ```bash
   aws s3 ls s3://my-idol-video-bucket/

   ```

4. **presign URL 発行（有効期限 1 時間）**

   ```bash
   aws s3 presign s3://my-idol-video-bucket/sample_video.mp4 --expires-in 3600

   ```

👉 presign URL を使えば、公開設定なしで一時的に動画を再生できます。

<!-- # pixabay -->
<!-- https://pixabay.com/videos/fire-sparks-forest-night-dark-236711/ -->
