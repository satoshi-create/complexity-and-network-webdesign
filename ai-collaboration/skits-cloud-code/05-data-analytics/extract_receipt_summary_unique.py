import json, csv, re
import pandas as pd

# =========================================================
# Step 1. Textract JSON を読み込み、BlocksからLINE要素を抽出
# =========================================================
with open("result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = [b for b in data["Blocks"] if b.get("BlockType") == "LINE"]

# =========================================================
# Step 2. OCRゆらぎ補正 + カテゴリ判定 + 金額抽出
# =========================================================
rows = []
for i, line in enumerate(lines):
    text = line.get("Text", "").strip()
    conf = line.get("Confidence", 0)

    # OCR誤認補正（OpenAl → OpenAI）
    text_lower = (
        text.lower()
        .replace("openal", "openai")
        .replace("open ai", "openai")
        .replace("0penai", "openai")
        .replace("serv1ce", "service")
    )

    # カテゴリ判定
    category = None
    if any(k in text_lower for k in ["openai", "api", "service", "credit", "usage"]):
        category = "AIサービス"
    elif any(k in text_lower for k in ["subtotal", "total", "tax"]):
        category = "集計項目"

    # 金額抽出
    amount = None
    match = re.search(r"[\$¥]([0-9]+\.?[0-9]*)", text)
    if match:
        amount = float(match.group(1))

    rows.append({"text": text, "category": category, "amount": amount, "confidence": conf})

# =========================================================
# Step 3. 「AIサービス」行と「金額」行を関連づける
# =========================================================
records = []
for i, row in enumerate(rows):
    if row["category"] == "AIサービス":
        # 次の行で金額が見つかる場合に紐づけ
        next_amount = None
        for j in range(i + 1, min(i + 3, len(rows))):
            if rows[j]["amount"] is not None:
                next_amount = rows[j]["amount"]
                break
        if next_amount:
            records.append({
                "category": "AIサービス",
                "amount": next_amount,
                "source_text": row["text"]
            })

# =========================================================
# Step 4. 重複削除・CSV出力
# =========================================================
df = pd.DataFrame(records).drop_duplicates(subset=["category", "amount"])
output_path = "receipt_summary_filtered_unique.csv"
df.to_csv(output_path, index=False)

print("✅ 抽出完了:", output_path)
if df.empty:
    print("⚠️ 抽出結果が空です。Textract出力に 'OpenAI API usage credit' + 金額行が含まれていますか？")
else:
    print("\n🎯 抽出結果プレビュー:")
    print(df)
