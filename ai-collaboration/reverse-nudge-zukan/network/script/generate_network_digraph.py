import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from matplotlib.patches import FancyArrowPatch
import matplotlib

# GUI描画バックエンド
matplotlib.use("TkAgg")
plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams['axes.unicode_minus'] = False

# --- CSV読み込み ---
characters_df = pd.read_csv("../data/characters_main5.csv")
relations_df = pd.read_csv("../data/character_relations.csv")

# --- ID → 名前辞書 ---
id_to_name = dict(zip(characters_df["id"], characters_df["name"]))

# --- 英語 → 日本語の関係タイプ変換 ---
relation_type_ja = {
    "rival": "対立",
    "duo": "相棒",
    "neutralizer": "中和",
    "healer": "癒し",
    "observer": "見守り",
    "sympathizer": "共感",
    "enabler": "正当化"
}

# --- グラフ作成（有向） ---
G = nx.DiGraph()

for _, row in characters_df.iterrows():
    G.add_node(row["id"], label=row["name"])

for _, row in relations_df.iterrows():
    label_ja = relation_type_ja.get(row["relation_type"], row["relation_type"])
    G.add_edge(row["source_id"], row["target_id"], label=label_ja)

# --- ラベル・レイアウト ---
node_labels = {n: d['label'] for n, d in G.nodes(data=True)}
edge_labels = nx.get_edge_attributes(G, 'label')
pos = nx.spring_layout(G, seed=42, k=1.8)

# --- 描画 ---
fig, ax = plt.subplots(figsize=(12, 9))

# ノード描画
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=3000, ax=ax)

# ノードラベル（白フチ）
for node, (x, y) in pos.items():
    label = node_labels.get(node, node)
    text = plt.text(x, y, label, fontsize=12, ha='center', va='center', fontfamily="Meiryo", color='black')
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),
        path_effects.Normal()
    ])

# 手動でエッジを描画（FancyArrowPatch使用）
for (u, v, data) in G.edges(data=True):
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        connectionstyle='arc3,rad=0.1',
        arrowstyle='-|>',
        color='gray',
        linewidth=1.5,
        mutation_scale=20
    )
    ax.add_patch(arrow)

    # エッジラベルを中央に描画（白フチ付き）
    label = data.get("label", "")
    x, y = (x1 + x2) / 2, (y1 + y2) / 2
    text = ax.text(x, y, label, fontsize=10, ha='center', va='center',
                   fontfamily="Meiryo", color='darkgreen')
    text.set_path_effects([
        path_effects.Stroke(linewidth=2.5, foreground='white'),
        path_effects.Normal()
    ])

# タイトル・レイアウト
ax.set_title("キャラクター相関ネットワーク図（FancyArrowPatch矢印対応）", fontsize=16)
plt.axis("off")
plt.tight_layout()
plt.savefig("character_network_fancyarrow.png", dpi=300, bbox_inches='tight')
plt.show()
