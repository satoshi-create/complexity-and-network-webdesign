# 🗺️ 3tsubo-farm/farm-map.md ｜畑ユニット配置図と MVP 位置

このドキュメントでは、**3 坪単位で構成される畑ユニット群の配置図**を記録し、今後の MVP 畑の増設・比較・連携を視覚的に把握できるようにします。

---

## 🌱 現在の畑構成

### 🟩 mvp-bed-01_kiri-mulch

- 📍 位置：東端、桐の木の根元近く
- ✅ 状態：稼働中（2025 年 4 月〜）
- 🔳 面積：約 2m × 5m（=10㎡）
- 📄 対応ドキュメント：`mvp-bed-01_kiri-mulch/`

---

## 🗺️ 畑ユニット配置図（仮想マップ）

```mermaid
flowchart TB
  A[北側道路]:::path

  subgraph 3tsubo-farm 区画
    B1[⬜ mvp-bed-01_kiri-mulch\n(桐の木ゾーン)]:::active
    B2[⬜ （未設置）]:::vacant
    B3[⬜ （未設置）]:::vacant
  end

  A --> B1
  B1 --> B2 --> B3

  classDef active fill:#d0f0c0,stroke:#228b22;
  classDef vacant fill:#f0f0f0,stroke:#ccc;
  classDef path stroke-dasharray: 5 5;
```

---

## 📌 管理ルール

- 1 ユニット＝およそ 3 坪（10㎡）を基準とする
- 各畝ごとに **固有 ID（mvp-bed-xx\_名称）** を付与
- 面積・構成・観察対象を記録し、**ユニット間比較**や**ゾーニング設計**に活用する

---

> 🛠️ 今後は、各ユニットに「生物相」「土壌条件」「作物レイアウト」の違いを持たせ、**実験区的に管理・可視化していく予定**です。
