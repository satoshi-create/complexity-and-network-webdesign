import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.font_manager as fm
import matplotlib
matplotlib.use("TkAgg")  # 明示的にGUIバックエンドを設定
import matplotlib

print(f"現在のバックエンド: {matplotlib.get_backend()}")
# 実際に使われているフォントを確認
print("現在のフォント:", plt.rcParams["font.family"])
# 明示的に日本語フォントを指定
plt.rcParams['font.family'] = 'Meiryo'
plt.rcParams['axes.unicode_minus'] = False  # マイナス記号も日本語フォントで出すため

df_shrine = pd.read_csv("../data/shrine_shitennoji-shichigu.csv")
df_deity = pd.read_csv("../data/deity.csv")
df_relation = pd.read_csv("../data/shrine_deities_shitennoji-shichigu.csv")


G = nx.Graph()

# ノード：神社
for _, row in df_shrine.iterrows():
    G.add_node(row["id"], name=row["name"], lat=row["lat"], lng=row["lng"])

deity_id_to_name = dict(zip(df_deity["id"], df_deity["name_ja"]))

# 同じ祭神を祀る神社同士をエッジで接続
from itertools import combinations

# deity_idごとに、どの神社がその神を祀っているかグループ化
for deity_id, group in df_relation.groupby("deity_id"):
    shrine_ids = group["shrine_id"].tolist()
    deity_name = deity_id_to_name[deity_id]
    # その神を共有している神社同士の全ての組み合わせにエッジを追加
    for a, b in combinations(shrine_ids, 2):
        # deity_id の情報をエッジ属性として追加（後で名前に変換可能）
        G.add_edge(a, b,label=deity_name)


# ID → 名称変換マップ
shrine_labels = {row["id"]: row["name"] for _, row in df_shrine.iterrows()}

edge_labels = nx.get_edge_attributes(G, 'label')

# springレイアウトで配置
pos = nx.spring_layout(G, k=1.6, seed=42)
fig = plt.figure(figsize=(12, 9))
ax = plt.gca()  # 明示的に現在のAxes取得

nx.draw(G, pos, labels=shrine_labels, with_labels=True, node_color="lightblue",font_size=12,bbox=dict(facecolor='white', edgecolor='none', alpha=0.7),ax=ax,font_family="Meiryo")
# nx.draw_networkx_edge_labels(
#     G, pos,
#     edge_labels=edge_labels,
#     font_size=10,
#     font_color="darkgreen",
#     ax=ax,
#     font_family="Meiryo",
# )

# ノードラベルを手描き（白フチ付き）
for node, (x, y) in pos.items():
    label = shrine_labels[node]
    text = plt.text(
        x, y, label,
        fontsize=12,
        ha='center', va='center',
        fontfamily="Meiryo",
        color='black'
    )
    text.set_path_effects([
        path_effects.Stroke(linewidth=3, foreground='white'),  # フチの色と太さ
        path_effects.Normal()
    ])


# エッジラベルを手描き（白フチ付き）
for (u, v, data) in G.edges(data=True):
    label = data.get("label", "")
    (x1, y1), (x2, y2) = pos[u], pos[v]
    x, y = (x1 + x2) / 2, (y1 + y2) / 2  # 中点
    text = plt.text(
        x, y, label,
        fontsize=10,
        ha='center', va='center',
        fontfamily="Meiryo",
        color='darkgreen'
    )
    text.set_path_effects([
        path_effects.Stroke(linewidth=2.5, foreground='white'),
        path_effects.Normal()
    ])



plt.margins(0.1)
# plt.title("神社×神々ネットワーク", fontsize=16)
ax.set_title("神社×神々ネットワーク", fontsize=16)  # ← plt.title() ではなく ax.set_title()
plt.axis("off")
plt.tight_layout()
# plt.savefig("shrine_network_demo_with_deity_en.png")
plt.savefig("shrine_network_with_relational_data_ja.png", dpi=300, bbox_inches='tight')
plt.show()
