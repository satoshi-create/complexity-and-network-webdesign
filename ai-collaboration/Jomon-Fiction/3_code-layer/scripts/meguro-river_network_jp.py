import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path

# ==== 日本語フォントの検索と設定 ====
jp_font_path = None
for f in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
    if any(name in f for name in ['NotoSansCJK', 'Noto Sans CJK JP', 'IPAexGothic', 'Takao', 'VL Gothic', 'Meiryo', 'YuGothic']):
        jp_font_path = f
        break

if jp_font_path:
    font_properties = fm.FontProperties(fname=jp_font_path)
    print(f"✅ 使用フォント: {font_properties.get_name()}")
else:
    print("⚠️ 日本語フォントが見つかりません。")
    font_properties = None


# === 🌐 ネットワークの定義 ===
G = nx.Graph()

# ノードの追加（遺跡・神社・貝塚など）
G.add_node('目黒不動遺跡', type='遺跡')
G.add_node('品川神社', type='神社')
G.add_node('大森貝塚', type='貝塚')
G.add_node('伊皿子貝塚', type='貝塚')
G.add_node('氷川遺跡', type='遺跡')
G.add_node('円融寺遺跡', type='遺跡')

# エッジの追加（関係性）
G.add_edge('目黒不動遺跡', '品川神社', relation='川沿い交易')
G.add_edge('目黒不動遺跡', '氷川遺跡', relation='湧水文化')
G.add_edge('品川神社', '大森貝塚', relation='湾岸の交易ランドマーク')
G.add_edge('品川神社', '伊皿子貝塚', relation='湾岸の交易ランドマーク')
G.add_edge('円融寺遺跡', '目黒不動遺跡', relation='癒しの流域圏')

# === 🖼️ 描画設定 ===
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)  # ノードの配置

# ノードとラベル描画
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2500,
    font_size=10,
    font_properties=font_properties  # ✅ 明示的に指定
)

# エッジラベル（関係性）を描画
edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,fontproperties=font_properties)

plt.title('Megurogawa Jomon Cultural Network', fontproperties=font_properties)
plt.tight_layout()

# === 💾 ファイル出力 ===
output_path = Path("meguro-river-network-jp.png")
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300)

print(f"✅ 日本語ネットワーク図を保存しました：{output_path.resolve()}")
