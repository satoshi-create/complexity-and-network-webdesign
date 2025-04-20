# 🍄 Fungi Network Visualizer｜菌糸ネットワーク・ビジュアライザー

This project visualizes fungal mycelium networks as ecological graphs, blending simplicity with biological realism.  
Inspired by real-world data and biological behavior, it models and renders fungal networks in 3D using Python and PyVista.  
Originally designed as a minimal working example in the "from-RDB-to-Network" journey, it has now sprouted into a more expressive tool — thanks to community contributions. 

本プロジェクトは、菌類の菌糸ネットワークを生態学的グラフとして可視化し、シンプルさと生物学的リアリズムを両立します。
実際の生態データや菌類のふるまいから着想を得て、PythonとPyVistaを用いて3Dモデル化・可視化を行います。
「from-RDB-to-Network」ジャーニーの中でMVP（最小動作例）として設計されましたが、コミュニティの協力により、より豊かなツールへと成長を始めています。

---

## 🧪 Features / 特徴

- Realistic 3D layouts of fungal mycelium networks  
  菌糸ネットワークをリアルな3D空間にレイアウト
- NetworkX-based graph modeling from CSV/JSON  
  CSV/JSON形式のデータからNetworkXでネットワーク構築
- Visual rendering using PyVista, optionally embedded in Streamlit  
  PyVistaを用いた描画（Streamlitとの連携も可能）
- Open for playful extensions and scientific exploration  
  拡張や創造的な応用、科学的探究に柔軟に対応

![Fungi Network Real](./image/fungi-network-real.png)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/github/satoshi-create/complexity-and-network-webdesign/blob/main/projects/from-rdb-to-network/fungi-network/notebooks/real-fungi-network.ipynb)

> A sample visualisation of a real fungal mycelium-like network using NetworkX  
> 実際の菌糸ネットワークに近い構造をNetworkXで可視化した例

---

## 📊 Goals｜プロジェクトの目的

- ✅ Visualize fungal networks as static graphs using NetworkX and matplotlib  
  ✅ NetworkXとmatplotlibで菌糸ネットワークを静的に可視化
- ✅ Start from simple CSV/JSON data formats for accessibility  
  ✅ CSV/JSON形式で誰でも編集可能な構成
- 🔄 Explore different network topologies (grid, tree, random)  
  🔄 グリッド・ツリー・ランダムなど多様な構造を探究
- 🛤️ Demonstrate a pathway from static data to interactive visualization  
  🛤️ 静的データからインタラクティブ表現へのステップを提示
- 🧪 Serve as a conceptual prototype for future data-driven network modeling  
  🧪 今後のネットワーク型モデリングに向けた概念的プロトタイプ

> Although this MVP uses CSV/JSON, the structure is compatible with RDB-based workflows (e.g. SQLite, Supabase) for future extension.  
> MVPはCSV/JSONベースですが、RDB（例：SQLite, Supabase）との統合も視野に入れた設計になっています。

---

## 🚀 MVP Scope & Steps｜MVPの構成とステップ

| Step | Description (EN)                                                                 | 説明（JP）                                               |
|------|----------------------------------------------------------------------------------|----------------------------------------------------------|
| 1️⃣   | Load node and edge data from `sample-network-nodes.csv` and `sample-network-edges.csv` | `sample-network-nodes.csv`と`sample-network-edges.csv`からデータを読み込む |
| 2️⃣   | Build a NetworkX graph with `node_type` and `weight` attributes                | `node_type`や`weight`属性を持つNetworkXグラフを構築             |
| 3️⃣   | Visualize with matplotlib (color-coded nodes, weighted edges)                 | matplotlibでノード色分け・エッジの重みを可視化                  |
| 4️⃣   | Export the result as PNG and embed in this README                            | 結果をPNG出力しREADMEに組み込み                             |
| 5️⃣   | Optionally run the same logic in a Colab notebook                            | 同じ処理をColabノートブックでも再現可能                      |

> 🧬 Fungal networks show us that intelligence isn’t centralized — it’s distributed, adaptive, and relational.  
> 菌糸ネットワークは、知性が集中ではなく分散・適応・関係性から生まれることを教えてくれます。これはOSSや共同設計の思想にもつながります。

---

## 📂 Structure｜ディレクトリ構成

- `data/`: Sample network datasets (`*.csv`, `*.json`)  
  サンプルネットワークデータ（CSV / JSON）
- `scripts/`: Python scripts for loading and visualizing with NetworkX  
  NetworkXを使った読み込み・可視化用のスクリプト
- `notebooks/`: Google Colab–ready interactive notebooks  
  Colab対応の対話型ノートブック

## 🧫 Want to take this further?｜さらに発展させるには？

- Add interactivity with D3.js, Dash, or Streamlit  
  D3.js, Dash, Streamlitでインタラクティブ化
- Convert CSV/JSON to RDB and explore query-driven graphs  
  CSV/JSONからRDBへ変換し、クエリベースでグラフ探索
- Use real-world ecological or mycological data  
  実際の菌類観察データや生態系データとの統合

## 📚 Data Source Citations｜データ出典

- Mesoscale analyses of fungal networks as an approach for quantifying phenotypic traits.  
  Sang Hoon Lee, Mark D. Fricker, Mason A. Porter.  
  Journal of Complex Networks, 2016. [bibtex]

Pull requests and ideas welcome! 🌱  
Pull Requestやアイデアも大歓迎です！🌱

**Tags:** `#network-thinking` `#mycelium` `#complexity` `#graph-theory` `#bio-inspired` `#mvp`

