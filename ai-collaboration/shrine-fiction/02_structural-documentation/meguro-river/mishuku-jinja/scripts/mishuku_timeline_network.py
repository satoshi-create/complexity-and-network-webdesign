import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.patches as mpatches


# 日本語フォント設定
plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams['axes.unicode_minus'] = False

# データ準備（例: mishuku_timeline_network.csvを読み込む）
df = pd.read_csv('../data/mishuku_timeline_network.csv')

# グラフ構築
G = nx.DiGraph()
for _, row in df.iterrows():
    G.add_node(row['source'], era=row['era'], label=row['source'])
    G.add_node(row['target'], era=row['era'], label=row['target'])
    G.add_edge(row['source'], row['target'], type=row['type'], note=row['note'], era=row['era'])

# カラー設定
era_colors = {"縄文": "forestgreen", "中世": "royalblue", "江戸": "darkorange", "近代": "crimson"}
node_colors = [era_colors.get(G.nodes[n]["era"], "gray") for n in G.nodes]

# 凡例（レジェンド）の定義
legend_handles = [
    mpatches.Patch(color='forestgreen', label='縄文'),
    mpatches.Patch(color='royalblue', label='中世'),
    mpatches.Patch(color='darkorange', label='江戸'),
    mpatches.Patch(color='crimson', label='近代')
]

# レイアウト
pos = nx.spring_layout(G, seed=42, k=1.5)

# 描画
plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1000, alpha=0.9)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')

for node, (x, y) in pos.items():
    label = G.nodes[node]['label']
    text = plt.text(x, y, label, fontsize=12, ha='center', va='center', color='black', fontfamily='Meiryo')
    text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='white'), path_effects.Normal()])

for (u, v, data) in G.edges(data=True):
    label = data.get('type', '')
    (x1, y1) = pos[u]
    (x2, y2) = pos[v]
    x, y = (x1 + x2) / 2, (y1 + y2) / 2
    text = plt.text(x, y, label, fontsize=10, ha='center', va='center', color='black', fontfamily='Meiryo')
    text.set_path_effects([path_effects.Stroke(linewidth=2.5, foreground='white'), path_effects.Normal()])

plt.title("三宿神社 時系列ネットワーク仮説図", fontsize=16)
plt.axis('off')
plt.legend(handles=legend_handles, loc='lower left', fontsize=12)
plt.savefig("mishuku_timeline_network.png", dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()
