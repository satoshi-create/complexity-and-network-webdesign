import json

import networkx as nx
import matplotlib.pyplot as plt

with open("../data/sample-network.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data["nodes"]
edges = data["links"]


# 1. 空の無向グラフ（Graph）を作成（有向にしたい場合は nx.DiGraph()）
G = nx.Graph()

# 2. ノードを追加
for node in nodes:
    G.add_node(node["id"], node_type=node["type"])

# 3. エッジ（ノード間の接続）を追加
for edge in edges:
    G.add_edge(edge["source"], edge["target"], weight=edge["weight"])

# 4. ノードのtypeごとに色分け（可視化のため）
color_map = {
    "core": "#4CAF50",     # 緑：中心部
    "branch": "#2196F3",   # 青：枝分かれ
    "tip": "#FFC107"       # 黄：末端
}

# 各ノードの色を、ノード属性（type）に応じて設定
node_colors = [color_map[G.nodes[n]["node_type"]] for n in G.nodes]
# 太さの指定：重みに比例して調整（スケーリング）
edge_weights = [G[u][v]["weight"] * 1.5 for u, v in G.edges]

# 5. グラフを描画する
plt.figure(figsize=(8, 6))
# spring_layout: ノードが自然に広がるよう配置（物理モデルに基づく）
pos = nx.spring_layout(G, seed=42,weight=None)
# ノード描画（色・サイズを設定）
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800)
# エッジ描画（接続線）
nx.draw_networkx_edges(G, pos,width=edge_weights)
# ラベル（ノードID）描画
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
plt.title("Fungi Network (Sample)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
