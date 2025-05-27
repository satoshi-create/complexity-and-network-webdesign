---

## 🇯🇵 日本語

```markdown
# 🗑️ machida-gomi-structure

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Part of CivicCommonsLab](https://img.shields.io/badge/CivicCommonsLab-ecosystem-blueviolet)](../)

> ごみ分別データを「生活コモンズ」として再構築するためのプロトタイプ。

---

## 🔄 プロジェクト概要

**machida-gomi-structure** は、**CivicCommonsLab** のサブプロジェクトです。
町田市のごみ分別 PDF を題材に、静的な行政資料を生活者の「環世界」に沿った構造化データ（CSV/JSON）へ変換することを目指します。

ごみカテゴリを単なるルールとしてではなく、**生態・社会構造** として捉え直すことで、行政データを私たちの日常コモンズとして再発見します。

---

## 🛠️ MVP ワークフロー

1️⃣ **OCR・テキスト抽出**
2️⃣ **基本的な整形**
3️⃣ **カテゴリ分類**
4️⃣ **CSV/JSON 出力**
5️⃣ **可視化（Mermaid.js / NetworkX）**
6️⃣ **ストーリー化・振り返り**

行政データの複雑さを単純化せずに構造化し、**市民にとって意味のある UX** を目指します。

---

## ⚙️ 技術スタック

- **Python**: OCR、pandas、JSON/CSV 出力
- **Mermaid.js**: フローダイアグラム
- **NetworkX**: 関係性ネットワークの可視化

---

## 📂 ディレクトリ構成

```plaintext
machida-gomi-structure/
├── data/
│   ├── raw/            # 元PDF
│   ├── ocr_text/       # 抽出テキスト
│   ├── csv/            # CSV出力
│   └── json/           # JSON出力
│
├── scripts/            # OCR・整形・分類・出力スクリプト
├── visualization/      # Mermaid・NetworkX可視化例
├── README.md           # このファイル
└── .gitignore
```
