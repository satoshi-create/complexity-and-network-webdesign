import camelot
import os

# PDFファイルのパス
pdf_path = "../data/raw/machida_gomi.pdf"

# 出力ディレクトリ
output_dir = "../data/csv"
os.makedirs(output_dir, exist_ok=True)

# PDF全ページから表を抽出
# flavor: 'lattice'（罫線あり）または 'stream'（罫線なし）を状況に応じて切り替える
tables = camelot.read_pdf(pdf_path, pages="all", flavor='stream')

print(f"✅ Tables found: {tables.n}")

# すべての表をCSVに出力
for i, table in enumerate(tables):
    output_file = os.path.join(output_dir, f"table_{i+1}.csv")
    table.to_csv(output_file)
    print(f"✅ Saved: {output_file}")

print("🎉 All tables converted to CSV!")
