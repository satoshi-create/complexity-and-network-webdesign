# ⚩ Shrine Network Visualizer

This project visualizes shrine-deity relationships as a cultural network rooted in geography and watershed logic.

📘 Read this in other languages:

- [🇯🇵 日本語](./README_ja.md)

---

## 🧪 Features

- Bipartite graph: **Shrines × Deities**
- Auto-generate edges between shrines sharing the same deity
- NetworkX-based modeling and export (.graphml, .png)
- Visualize with matplotlib or Jupyter Notebook
- Ready for geospatial overlays (GSI Maps, GeoJSON)

![Shrine Network](./public/images/shrine_network_demo_with_deity_en.png)
![Shrine Network](./public/images/shrine_network_with_relational_data_ja.png)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satoshi-create/complexity-and-network-webdesign/blob/create/shrine-network/projects/from-rdb-to-network/shrine-network/notebooks/shrine_network_with_relational_data.ipynb)

---

## 🧩 Data Model

Below is the ER diagram of the three core CSVs used to construct the shrine-deity network:

```mermaid
erDiagram
  SHRINES ||--o{ SHRINE_DEITY : includes
  DEITY ||--o{ SHRINE_DEITY : associated_with

  SHRINES {
    string id PK "Shrine ID"
    string name "Shrine Name (Japanese)"
    string name_en "Shrine Name (English)"
    float latitude "Latitude"
    float longitude "Longitude"
    string type "shrine or temple"
  }

  DEITY {
    string id PK "Deity ID"
    string name_ja "Deity Name (Japanese)"
    string name_en "Deity Name (English)"
  }

  SHRINE_DEITY {
    string shrine_id FK
    string deity_id FK
    string note "optional: special role or description"
  }
```

---

## 📊 Goals

- Build cultural networks from CSV/JSON data
- Explore spatial-symbolic patterns across shrine locations
- Prototype for multi-layered cultural graphs

---

## 🚀 MVP Steps

| Step | Description |
|------|-------------|
| 1    | Load shrine and deity data from CSV |
| 2    | Create edges between shrines sharing the same deity |
| 3    | Generate NetworkX graph |
| 4    | Export the graph (PNG/graphml) |
| 5    | Visualize or map with Jupyter or GSI tools |

---

## 🏠 Shrine Examples

<div align="center">
<table>
  <tr>
    <td align="center">
      <img src="./public/images/kamimeguro-hikawa-shrine/kamimeguro-hikawa-shrine_8.jpg" width="400"><br/>
      <strong>Kamimeguro Hikawa Shrine</strong><br/>
      Susanoo-no-Mikoto
    </td>
    <td align="center">
      <img src="./public/images/komatsunagi-shrine/komatsunagi-shrine_7.jpg" width="400"><br/>
      <strong>Komatsunagi Shrine</strong><br/>
      Takemikazuchi-no-Kami
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./public/images/meguro-fudoson/meguro-fudoson_11.jpg" width="400"><br/>
      <strong>Meguro Fudōson (Ryūsenji)</strong><br/>
      Fudō Myōō
    </td>
    <td align="center">
      <img src="./public/images/mishuku-shrine/mishuku-shrine_4.jpg" width="400"><br/>
      <strong>Mishuku Shrine</strong><br/>
      Ōyamatsumi-no-Kami
    </td>
  </tr>
</table>
</div>

---

## 🗾 GSI Mapping

![mapping](./public/images/shrine-locations-mapping.JPG)

👉 [View on GSI Maps (Meguro Fudō Area)](https://maps.gsi.go.jp/#14/35.635012/139.685755/&base=std&ls=std%7Canaglyphmap_color%2C0.47%7Cexperimental_landformclassification1%2C0.56&blend=0&disp=111&lcd=experimental_landformclassification1&vs=c1g1j0h0k0l0u0t0z0r0s0m0f0)  
👉 [View on Google Map (Meguro Fudō Area)](https://maps.app.goo.gl/ekTJ6fZX6zTnPSL66)  
📎 [Download shrine-locations.geojson](./data/shrine_meguro-river.geojson)

> You can upload the above GeoJSON file to GSI maps to display shrine locations as a custom overlay.

---

## 📂 Structure

```
shrine-network/
├── data/        # CSV, JSON data of shrines & deities
├── notebooks/   # Jupyter notebooks for exploration
├── public/images/  # Shrine photos, GSI screenshots
└── README.md
```

---

## 🧠 Future Ideas

- GeoJSON & GSI for interactive mapping
- Extend to temples and ruins
- D3.js or Streamlit for tourism-focused apps

---

## 🗂 Sources

- Official websites of shrines
- GSI maps by Japan GSI

Pull requests and ideas welcome! 🌿

**Tags:** `#network-thinking` `#shinto` `#gis` `#bipartite-graph` `#cultural-data` `#open-data`

📘 Read this in Ja
