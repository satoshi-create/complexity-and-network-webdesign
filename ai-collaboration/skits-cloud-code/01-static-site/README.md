# 静的サイト公開

S3 を使って簡単に HTML を公開する手順。

```mermaid
graph TD
    A[HTMLファイル index.html] -->|アップロード| B[S3 Bucket]
    B -->|公開設定| C[Static Website Endpoint]
    C --> D[ブラウザでアクセス]
```
