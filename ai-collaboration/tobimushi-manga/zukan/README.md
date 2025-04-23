# 🌱 トビムシマンガ ZUKAN 図鑑 / Tobimushi Manga ZUKAN Encyclopedia

このディレクトリは、トビムシマンガの世界観に登場するキャラクターや道具を体系的に整理・保存する図鑑です。  
This directory contains a structured encyclopedia of characters and tools from the Tobimushi Manga universe.

---

## 🗂 ディレクトリ構成 / Directory Structure

```
zukan/
├── characters/        # キャラクター全般 / All Characters
├── tools/             # 道具・装備 / Tools and Devices
├── templates/         # テンプレート / Templates for new entries
├── index.json         # 全アイテムのメタ情報一覧 / Index of all items
└── README.md          # このファイル / This README
```

---

## 🧭 使い方 / How to Use

### 🧑‍🎨 キャラクター / Characters
- `characters/{id}/` ディレクトリに `profile.md`（日英併記）と `metadata.json`（属性情報）を配置してください。  
  Place `profile.md` (bilingual) and `metadata.json` (attribute data) in each `characters/{id}/` directory.
- 画像は `images/` に `icon.png` と `full.png` を保存します。  
  Save `icon.png` and `full.png` in the `images/` folder.

### 🧰 道具 / Tools
- 道具も `tools/{id}/` に `profile.md` と `metadata.json` を配置します。  
  Tools also go in `tools/{id}/` with the same structure.

### 🧩 テンプレート / Templates
- 新規アイテムを追加する際には、対応するテンプレートを参考にしてください。  
  Use appropriate templates when adding new items:
  - `character-template.md`
  - `tool-template.md`

---

## 🛠 index.json について / About `index.json`

`zukan/index.json` は、登録されたすべてのアイテムのメタ情報を集約するインデックスです。  
`zukan/index.json` is a metadata index of all registered items.

フロントエンドでの一覧表示やタグ別検索に利用されます。  
Used for frontend displays and tag-based filtering.

---

## 📚 登録済みアイテム一覧 / Registered Items

### 🧑‍🎨 キャラクター / Characters
| Image | Name | Description |
|-------|------|-------------|
| ![tobino](./1_characters/tobino/images/tobino.png) | **トビノ / Tobino** | 跳ねるように旅をする土壌ノマド。菌糸ネットワークの沈黙に気づいた存在。<br>A soil-dwelling nomad who leaps through ecosystems and senses fungal silence.

### 🧰 道具 / Tools
| Image | Name | Description |
|-------|------|-------------|
| ![resonance-tuner](./2_tools/resonance-tuner/images/resonance-tuner.png) | **共鳴チューナー / Resonance Tuner** | 菌糸ネットワークの異常を感知するための生体センサー装置。<br>A biosensory device that detects disruptions in the mycorrhizal network.

---

## 💬 コントリビューション / Contributions Welcome!

- キャラクターや道具の追加・翻訳・画像提供などの参加を歓迎します。  
  Contributions for adding items, translations, or visuals are welcome.
- フォーマットや追加方法に不明点がある場合は、テンプレートまたは Issue にてご相談ください。  
  If unsure, refer to templates or open an issue.

---

## 🌐 関連リンク / Related Links

- [Tobimushi Manga Main Repository](https://github.com/satoshi-create/tobimushi-manga) – トビムシマンガ本編のリポジトリ / Main manga project repository
- [CANW Project](https://github.com/satoshi-create/CANW) – 複雑系とネットワークの視点から文化を捉えるプロジェクト / Project for cultural analysis via complexity and networks

