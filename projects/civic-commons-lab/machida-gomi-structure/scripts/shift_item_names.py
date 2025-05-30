import pandas as pd  # pandasをインポート（CSV操作・表処理のため）

# CSVファイルの読み込み
file_path = "../data/csv/table_all.csv"  # 読み込むCSVファイルのパス（必要に応じて書き換え）
df = pd.read_csv(file_path, encoding="utf-8", header=None)  # ヘッダ行がないCSVなので header=None

# カテゴリ列（例: インデックス4）で「拠点回収」と書かれた行を検出する
category_col_index = 3  # カテゴリ列のインデックス（0始まりで5列目）
item_col_index = 1      # 品名列のインデックス（0始まりで2列目）

# カテゴリ列に「拠点回収」とある行のインデックス番号を取得
拠点回収_indices = df[df[category_col_index] == "拠点回収"].index.tolist()

# 各「拠点回収」行に対して、直前の行にある品名を「拠点回収行と同じ行」にコピーする
for idx in 拠点回収_indices:
    上の行_idx = idx - 1  # 1行上のインデックス
    if 上の行_idx >= 0:  # 先頭行を超えないようにチェック
        品名 = df.at[上の行_idx, item_col_index]  # 1行上の品名を取得
        # 1行下ではなく「同じ行」にコピーする
        df.at[idx, item_col_index] = 品名
        # 元の品名セルを空欄にする
        df.at[上の行_idx, item_col_index] = None


# （必要なら空行を削除）
df_cleaned = df.dropna(how='all')  # 全列がNaNの行を削除

# 整形後の先頭10行を確認
print(df_cleaned.head(10))

# （必要ならCSVに出力）
df_cleaned.to_csv("output.csv", index=False, header=False, encoding="utf-8-sig")
