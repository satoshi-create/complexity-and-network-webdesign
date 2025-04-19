# ⚩ Shrine Network Visualizer / 神社ネットワーク・ビジュアライザー

This project visualizes shrine-deity relationships as a cultural network rooted in geography and watershed logic.
このプロジェクトは、神社と神々の関係を地形や流域の視点から結びなおし、文化的ネットワークとして可視化することを目的とします。

---

## 🧪 Features / 特徴

- Bipartite graph: **Shrines × Deities**
  神社と神々の二層構造ネットワーク
- Auto-generate edges between shrines sharing the same deity
  同じ神を祭る神社同士を自動で繋ぐ
- NetworkX-based modeling and export (.graphml, .png)
  NetworkX を使ったグラフ生成とエクスポート
- Visualize with matplotlib or Jupyter Notebook
  matplotlib、Jupyter Notebook による可視化
- Ready for geospatial overlays (GSI Maps, GeoJSON)
  地理院地図や GeoJSON との連携も可能

---

## 📊 Goals / 目標

- Build cultural networks from CSV/JSON data
  CSV/JSON による文化ネットワークの構築
- Explore spatial-symbolic patterns across shrine locations
  神社配置における地形的、象徴的パターンを探索
- Prototype for multi-layered cultural graphs
  多層的文化グラフのプロトタイプ

---

## 🚀 MVP Steps / MVP のステップ

| Step | Description (EN / JP)                                         |
| ---- | ------------------------------------------------------------- |
| 1    | Load shrine and deity data from CSV / CSV データを読み込む    |
| 2    | Create edges for shared deities / 同神社をエッジで繋ぐ        |
| 3    | Generate NetworkX graph / NetworkX でグラフ生成               |
| 4    | Export graph / グラフゞエクスポート                           |
| 5    | Visualize or map with Jupyter, GSI / ノートブックや地図と連携 |

---

## 🏠 Shrine Examples / 神社の例

### Kamimeguro Hikawa Shrine / 上目黒氷川神社

![kamimeguro](./images/kamimeguro-hikawa.jpg)

- Deity: Susanoo / 神: 素斗明神
- On the edge of a plateau / 台地の端に位置

### Komatsunagi Shrine / 駒続神社

![komatsunagi](./images/komatsunagi-shrine.jpg)

- Deity: Takemikazuchi / 神: 武鬻鍬神
- Located in a valley area / 谷地形に守られた場所

### Meguro Fudouson / 目黒不動寺

![meguro](./images/meguro-fudoson.jpg)

- Buddhist temple with waterfall & escarpment / 滝や崖線による靈場性

### Mishuku Shrine / 三富神社

![mishuku](./images/mishuku-shrine.jpg)

- Deity: Ooyamatsumi / 神: 大山縁神
- Between cliffs and valleys / 崖線と谷の間に復本

---

## 🗾 GSI Mapping Example / 国土地理院マッピング例

![mapping](./images/shrine-locations-mapping.JPG)

Using GSI maps to overlay shrine locations helps reveal geographic patterns.
国土地理院の地図に神社を重ねることで、地形的な配置パターンを取り出せます。

---

## 📂 Structure / ファイル構成

```
shrine-network/
├── data/        # CSV, JSON data of shrines & deities
├── scripts/     # Network building scripts
├── notebooks/   # Jupyter notebooks for exploration
├── images/      # Shrine photos, GSI screenshots
└── README.md
```

---

## 🧠 Future Ideas / 発展案

- GeoJSON & GSI for interactive mapping / 地図上での動的可視化
- Extend to temples, ruins / 寺院や違跡も統合
- D3.js, Streamlit for tourism / 観光対応アプリへの発展

---

## 🗂 Sources / データ出典

- Open shrine data from Tokyo / 東京の開放データ
- Official websites of shrines / 各神社公式情報
- GSI maps by Japan GSI / 国土地理院地図

Pull requests and ideas welcome! プルリクエストやアイディア大歓迎です！

**Tags:** `#network-thinking` `#shinto` `#gis` `#bipartite-graph` `#cultural-data` `#open-data`
