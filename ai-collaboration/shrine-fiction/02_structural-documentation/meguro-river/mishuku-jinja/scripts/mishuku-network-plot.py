import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import matplotlib.patheffects as path_effects
import matplotlib

# 日本語フォントを指定（環境に合わせて変更可能）
plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams['axes.unicode_minus'] = False

# CSVファイルを読み込む
csv_path = '../data/mishuku_network.csv'  # ローカル用にパスを書き換えてください
network_data = pd.read_csv(csv_path)

# 有向グラフを作成
G = nx.DiGraph()

# ノードとエッジを追加
for _, row in network_data.iterrows():
    G.add_node(row['source'], label=row['source'], layer=row['layer'])
    G.add_node(row['target'], label=row['target'], layer=row['layer'])
    G.add_edge(row['source'], row['target'], label=row['type'])

# レイヤーによるノードの色分け
color_map = []
for node in G.nodes(data=True):
    if node[1]['layer'] == '自然層':
        color_map.append('skyblue')
    elif node[1]['layer'] == '仮説層':
        color_map.append('lightgreen')
    else:
        color_map.append('lightgray')

# レイアウト設定
pos = nx.spring_layout(G, seed=42)

# 図のサイズを指定
plt.figure(figsize=(12, 8))

# ノードを描画
nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=1000, alpha=0.9)

# エッジを描画
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')

# ノードラベル（白フチ付き）
for node, (x, y) in pos.items():
    label = G.nodes[node]['label']
    text = plt.text(x, y, label,
                    fontsize=12,
                    ha='center', va='center',
                    fontfamily='Meiryo',
                    color='black')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

# エッジラベル（白フチ付き）
for (u, v, data) in G.edges(data=True):
    label = data.get('label', '')
    (x1, y1) = pos[u]
    (x2, y2) = pos[v]
    x, y = (x1 + x2) / 2, (y1 + y2) / 2
    text = plt.text(x, y, label,
                    fontsize=10,
                    ha='center', va='center',
                    fontfamily='Meiryo',
                    color='black')
    text.set_path_effects([
        path_effects.Stroke(linewidth=2.5, foreground='white'),
        path_effects.Normal()
    ])

# レイヤーに対応した凡例を追加
legend_handles = [
    mpatches.Patch(color='skyblue', label='自然層'),
    mpatches.Patch(color='lightgreen', label='仮説層')
]
plt.legend(handles=legend_handles, loc='lower left', fontsize=12)

plt.title("三宿神社 流域ネットワーク仮説図", fontsize=16)
plt.axis('off')
plt.savefig("mishuku_shrine_network.png", dpi=300, bbox_inches='tight')
plt.show()
