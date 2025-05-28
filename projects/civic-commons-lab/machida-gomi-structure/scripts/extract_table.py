import camelot

# PDFファイルのパス
pdf_path = "../data/raw/machida_gomi.pdf"

# PDFの1ページ目の表を抽出
tables = camelot.read_pdf(pdf_path, pages="1", flavor='stream')  # 'lattice' も試せる

# 抽出されたテーブルの数を表示
print(f"Tables found: {tables.n}")

# CSVとして出力
for i, table in enumerate(tables):
    output_file = f"table_{i+1}.csv"
    table.to_csv(output_file)
    print(f"✅ Saved: {output_file}")
