# 🍄 Fungi Network Visualizer

This project visualizes fungal mycelium networks as ecological graphs, combining simplicity with biological realism.  
Inspired by real-world data and fungal behavior, it uses Python and PyVista to model and render 3D representations of fungal networks.  
Originally created as an MVP (minimum viable prototype) in the "from-RDB-to-Network" journey, it has started to grow into a more expressive and extensible tool — thanks to community contributions.

📘 Read this in other languages:

- [🇯🇵 日本語](./README_ja.md)

---

## 🧪 Features

- Realistic 3D layouts of fungal mycelium networks (via PyVista)
- Network construction using NetworkX from CSV/JSON formats
- Streamlit integration for optional interactive visualization
- Flexible structure for extensions, scientific exploration, or creative applications

![Fungi Network Real](./image/fungi-network-real.png)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satoshi-create/complexity-and-network-webdesign/blob/main/projects/from-rdb-to-network/fungi-network/notebooks/real-fungi-network.ipynb)

> A visual example of a fungal mycelium-like structure rendered using NetworkX

---

## 📊 Project Goals

- ✅ Visualize fungal networks as static graphs using NetworkX and matplotlib
- ✅ Accept simple CSV/JSON input formats for accessibility
- 🔄 Explore diverse topologies: grid, tree, random, etc.
- 🛤️ Demonstrate pathways from static to interactive network visualization
- 🧪 Serve as a conceptual prototype for data-driven network modeling

> Though CSV/JSON is used in the MVP, it is designed to be compatible with RDB workflows (e.g. SQLite, Supabase) for future integration.

---

## 🚀 MVP Scope & Steps

| Step | Description |
|------|-------------|
| 1️⃣   | Load node and edge data from `sample-network-nodes.csv` and `edges.csv` |
| 2️⃣   | Build a NetworkX graph with `node_type` and `weight` attributes |
| 3️⃣   | Visualize using matplotlib (color-coded nodes, weighted edges) |
| 4️⃣   | Export results as PNG and embed in this README |
| 5️⃣   | Optionally reproduce in a Colab notebook |

> 🧬 Fungal networks teach us that intelligence isn’t centralized — it's distributed, adaptive, and relational.  
> A lesson that also applies to OSS and decentralized design thinking.

---

## 📂 Project Structure

- `data/`: Sample datasets in CSV and JSON format
- `scripts/`: Python scripts for graph construction and visualization
- `notebooks/`: Colab-ready interactive notebooks

---

## 🧫 Future Possibilities

- Add interactivity with D3.js, Dash, or Streamlit
- Convert CSV/JSON to RDB and explore query-based networks
- Integrate with real-world ecological or fungal datasets

---

## 📚 Data Source Citation

- Mesoscale analyses of fungal networks as an approach for quantifying phenotypic traits.  
  Sang Hoon Lee, Mark D. Fricker, Mason A. Porter.  
  Journal of Complex Networks, 2016.

---

Pull requests and ideas welcome! 🌱

**Tags:** `#network-thinking` `#mycelium` `#complexity` `#graph-theory` `#bio-inspired` `#mvp`

📘 Read this in Japanese: [README.ja.md](./README.ja.md)
