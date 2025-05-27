---

## 🇯🇵 日本語

```markdown
<p align="center">
  <img src="https://github.com/satoshi-create/complexity-and-network-webdesign/blob/main/docs/branding-mvp-launch/images/logos/logo_cultural-emergent.png" alt="CANWロゴ" width="100"/>
</p>

<h1 align="center">🌐 CivicCommonsLab</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Part of CANW](https://img.shields.io/badge/CANW-ecosystem-blueviolet)](https://github.com/satoshi-create/complexity-and-network-webdesign)
[![Wiki](https://img.shields.io/badge/Wiki-Explore%20More-blue)](https://github.com/satoshi-create/complexity-and-network-webdesign/wiki)
![Contributors](https://img.shields.io/github/contributors/satoshi-create/complexity-and-network-webdesign?color=brightgreen)

📘 他言語版:

* [🇺🇸 English](./README.md)

> CivicCommonsLab: 行政資料を「生活コモンズ」として再構築する実験室。
>

本プロジェクトは **CANW**（Complexity And Network Webdesign）の一部です。
CANW全体の構想やコンセプトは [root README](https://github.com/satoshi-create/complexity-and-network-webdesign) を参照してください。

---

## 🔄 概要: CivicCommonsLab

**CivicCommonsLab** は、地域行政資料を「生活世界（環世界）」に根差した **コモンズ** として再構築する試みです。
堅苦しい行政資料（例：ごみ分別 PDF など）を、生活者の目線でよりアクセスしやすく、相互接続的で意味のある形に変換します。

---

## 🧪 現在の焦点: machida-gomi-structure

最初のプロトタイプ [**machida-gomi-structure**](./machida-gomi-structure) は、町田市のごみ分別 PDF を題材にしています。
OCR でテキストを抽出し、カテゴリ分類・正規化して CSV/JSON に構造化。
**Mermaid.js** や **NetworkX** を使い、行政資料に隠れた分類ロジックを可視化し、制度文脈の複雑さをそのまま表現します。

---

## 🛠 技術と協働

使用ツール:

- Python（OCR、pandas、JSON/CSV 出力）
- Mermaid.js、NetworkX による可視化
- Jupyter Notebook による AI と人間の協働実験

強調するポイント:

- 複雑さを単純化せず、構造化・可視化する
- 人間 ×AI 協働による背景の「物語」の抽出
- 制度と生活世界をつなぐ UX 視点

📎 GitHub リポジトリ:
[https://github.com/satoshi-create/civic-commons-lab](https://github.com/satoshi-create/civic-commons-lab)

---

## 🌐 エコシステムフロー（Mermaid）

```mermaid
graph TD
  A[行政PDFデータ] --> B[OCR・テキスト整形]
  B --> C[カテゴリ分類・構造化]
  C --> D[可視化 (Mermaid.js, NetworkX)]
  D --> E[リフレクション・UXストーリー化]
  E --> F[CANW全体アーキテクチャとの接続]

  subgraph プロトタイプ
    P1[machida-gomi-structure]
  end

  C --> P1
```
