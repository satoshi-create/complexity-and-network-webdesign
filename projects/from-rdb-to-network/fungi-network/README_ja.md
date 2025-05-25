# 🍄 Fungi Network Visualizer｜菌糸ネットワーク・ビジュアライザー

本プロジェクトは、菌類の菌糸ネットワークを生態学的グラフとして可視化し、シンプルさと生物学的リアリズムの両立を目指すツールです。  
実際の観察データや菌類のふるまいから着想を得て、Python + PyVista により3Dで菌糸ネットワークを描画します。  
「from-RDB-to-Network」のジャーニーでMVP（最小動作例）として生まれましたが、コミュニティの協力により豊かなツールへと進化しています。

📘 他の言語で読む:

- [🇺🇸 English](./README.md)
---

## 🧪 特徴

- 菌糸ネットワークをリアルな3D空間にレイアウト（PyVista）
- CSV/JSON形式からNetworkXでネットワーク構築
- Streamlitとの連携も視野に入れた柔軟な設計
- 拡張や応用、科学的探究にも開かれたプロジェクト

![Fungi Network Real](./image/fungi-network-real.png)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satoshi-create/complexity-and-network-webdesign/blob/main/projects/from-rdb-to-network/fungi-network/notebooks/real-fungi-network.ipynb)

> NetworkXで構築した実際の菌糸ネットワークに近い構造の可視化例

---

## 📊 プロジェクトの目的

- ✅ NetworkXとmatplotlibで静的にネットワークを可視化
- ✅ CSV/JSON形式のシンプルな入力でデータを編集可能に
- 🔄 グリッド・ツリー・ランダム構造など多様なネットワーク形状を探究
- 🛤️ 静的可視化からインタラクティブな表現への道筋を示す
- 🧪 データ駆動型ネットワークモデリングへの概念的プロトタイプ

> 現在はCSV/JSONベースですが、将来的にはRDB（SQLite, Supabase等）との統合も視野に入れています。

---

## 🚀 MVPの構成とステップ

| ステップ | 説明 |
|----------|------|
| 1️⃣       | `sample-network-nodes.csv` / `edges.csv` からデータを読み込み |
| 2️⃣       | `node_type` や `weight` 属性付きのNetworkXグラフを構築 |
| 3️⃣       | matplotlibでノード色分け・エッジ重みを視覚化 |
| 4️⃣       | 結果をPNGとして出力しREADMEに埋め込み |
| 5️⃣       | 同様の処理をGoogle Colab上でも実行可能 |

> 🧬 菌糸ネットワークは、知性が“中央集権的”ではなく、分散的・適応的・関係性駆動であることを示しています。  
> この思想はOSSや分散的な設計思考にも通じます。

---

## 📂 ディレクトリ構成

- `data/`: CSV・JSON形式のサンプルネットワークデータ
- `scripts/`: NetworkXによるグラフ構築と可視化用スクリプト
- `notebooks/`: Google Colab対応のノートブック

---

## 🧫 発展的な活用例

| 難易度 | テーマ | Pythonツール例 | 具体的にできること | 可視化・分析による期待効果 |
|--------|--------|----------------|--------------------|----------------------------|
| 🟢 低 | 地図ベースの菌類分布表示 | pandas<br>geopandas<br>folium | - 菌類の採取地点をマッピング<br>- 基本的な地理的分布を確認 | - 地理的な分布パターンの把握<br>- 分布傾向の視覚化 |
| 🔵 中 | 空間的近接性によるネットワーク構築 | geopandas<br>networkx<br>shapely | - 緯度・経度情報をもとに菌類ネットワークを構築<br>- 空間的距離によるエッジ設定（例: 半径10km以内） | - 地理的ネットワーク構造の可視化<br>- 空間的な菌類の関係性の理解 |
| 🔵 中 | GISレイヤーとの重ね合わせ | rasterio<br>geopandas<br>gdal | - 土壌、植生などの環境データと菌類分布を統合<br>- ラスター・ベクターデータを解析 | - 生態系全体の文脈における菌類ネットワークの役割の把握<br>- 環境要因との相関可視化 |
| 🔴 高 | 空間ネットワークの動的解析 | dynetx<br>temporal_networkx<br>folium.plugins | - 時間的な分布変化をネットワークとしてモデル化<br>- 季節性や成長過程の動的ネットワーク分析 | - 菌類ネットワークの動的進化の理解<br>- 季節変動や環境変化への応答を可視化 |
| 🔴 高 | Webアプリ化による共有・分析基盤 | streamlit<br>dash<br>plotly | - 地図・ネットワークをWeb上でインタラクティブに表示<br>- 関連データを可視化・操作するWebツールを構築 | - 研究・教育用のオープンな可視化基盤<br>- リアルタイム解析やフィードバックの可能性 |



---

## 📚 データ出典

- Mesoscale analyses of fungal networks as an approach for quantifying phenotypic traits.  
  Sang Hoon Lee, Mark D. Fricker, Mason A. Porter.  
  Journal of Complex Networks, 2016.

---

Pull Requestやアイデアも大歓迎です！🌱

**タグ:** `#network-thinking` `#mycelium` `#complexity` `#graph-theory` `#bio-inspired` `#mvp`
