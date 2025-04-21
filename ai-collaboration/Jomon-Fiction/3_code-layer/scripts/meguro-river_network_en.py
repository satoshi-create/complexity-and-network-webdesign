import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# === Define Network in English ===
G = nx.Graph()

# Nodes (Archaeological and Ritual Sites)
G.add_node('Meguro Fudo Site', type='archaeological site')
G.add_node('Shinagawa Shrine', type='shrine')
G.add_node('Omori Shell Mound', type='shell mound')
G.add_node('Isarago Shell Mound', type='shell mound')
G.add_node('Hikawa Site', type='archaeological site')
G.add_node('Enyuji Site', type='archaeological site')

# Edges with relationships
G.add_edge('Meguro Fudo Site', 'Shinagawa Shrine', relation='Trade route along the river')
G.add_edge('Meguro Fudo Site', 'Hikawa Site', relation='Springwater culture')
G.add_edge('Shinagawa Shrine', 'Omori Shell Mound', relation='Bay trading landmark')
G.add_edge('Shinagawa Shrine', 'Isarago Shell Mound', relation='Bay trading landmark')
G.add_edge('Enyuji Site', 'Meguro Fudo Site', relation='Healing valley connection')

# === Draw Network ===
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)

# Nodes and labels
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2500,
    font_size=10
)

# Edge labels
edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Title and layout
plt.title('Megurogawa Jomon Cultural Network')
plt.tight_layout()

# Save image
output_path = Path("meguro-river-network-en.png")
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, dpi=300)
plt.show()

print(f"✅ Saved: {output_path.resolve()}")
