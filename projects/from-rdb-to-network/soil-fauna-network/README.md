# 🕼 Soil Fauna Network Visualizer

This project visualizes soil fauna interaction networks as ecological graphs, inspired by the complexity of belowground life.
As a sister project to the “Fungi Network Visualizer,” it explores how micro- and mesofauna co-create dynamic ecosystems through predation, mutualism, and detritus processing.
Originally designed as an MVP in the "from-RDB-to-Network" journey, this tool demonstrates how relational ecological data can be transformed into meaningful network structures.

📘 Read this in other languages:

- [🇯🇵 日本語](./README_ja.md)


---

## 🧪 Features

* Species interaction modeling from relational CSV data
* NetworkX-based construction with trophic and ecological roles
* White-stroked Japanese labels for full readability
* Static graph visualization with matplotlib (PNG export ready)
* Ready-to-run Colab notebook and customizable scripts

![Soil Fauna Network](./public/images/soil-fauna-network_demo_en.png)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/satoshi-create/complexity-and-network-webdesign/blob/soil-fauna-network/projects/from-rdb-to-network/soil-fauna-network/notebooks/soil-fauna-network_demo_en.ipynb)

> A minimal working example showing how species interaction networks emerge from simple CSV-based relational data.

---

## 🤩 Data Model

Below is the ER diagram of the three core CSVs used to construct the soil fauna interaction network.

```mermaid
erDiagram

    SPECIES {
        int id PK
        string scientific_name
        string japanese_name
        string common_name
        string taxonomy
        string taxonomy_en
        string functional_role
        string functional_role_en
        string note
    }

    INTERACTION {
        int source_id FK
        int target_id FK
        string relation_type
        string description
    }

    SITE_SPECIES {
        string site_id FK
        int species_id FK
        int abundance
        date date
        string note
    }

    SITES {
        string site_id PK
        string name
        float latitude
        float longitude
        string soil_type
        string note
    }

    SPECIES ||--o{ INTERACTION : is_source_of
    SPECIES ||--o{ INTERACTION : is_target_of
    SPECIES ||--o{ SITE_SPECIES : occurs_in
    SITES ||--o{ SITE_SPECIES : contains
```

---

## 📊 Goals

* ✅ Visualize species interactions in Japanese using NetworkX
* ✅ Start from intuitive, editable CSV files for species and relations
* ✅ Highlight ecological roles with color coding and font effects
* 🛤️ Connect to real site data with `site_species.csv` and `sites.csv`
* 🔁 Encourage extensions with ecological or educational data

> While this MVP is static and small-scale, its structure supports scaling into full RDB-backed networks and interactive visualization environments.

---

## 🚀 MVP Scope & Steps

| Step | Description (EN)                                                           |
| ---- | -------------------------------------------------------------------------- |
| 1️⃣  | Load species and interaction data from `species.csv` and `interaction.csv` |
| 2️⃣  | Construct a directed graph with roles and labels (Japanese names)          |
| 3️⃣  | Visualize the network with node colors and white-outlined text             |
| 4️⃣  | Export to PNG and embed as documentation asset                             |
| 5️⃣  | Run and edit the logic in `notebooks/soil-fauna-network-demo-ja.ipynb`     |

> 🐛 Soil fauna embody decentralized, adaptive systems. Mapping their interactions reflects not only biodiversity, but a model of collaborative intelligence.

---

## 📂 Structure

* `data/`: CSV files for species, interactions, and site-specific occurrences
* `scripts/`: Python script for visualization and export (static PNG)
* `notebooks/`: Colab-friendly Jupyter notebook with step-by-step execution

---

## 🧠 Want to take this further?

| 🥇 Difficulty | 🌐 Theme                   | 🛠️ Python Tools                                           | 🔧 What You Can Do                                                   | 💡 Expected Effects of Visualization & Analysis                        |
|----------------|--------------------------|------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| 🟢 Low         | **Basic Visualization**  | `matplotlib`, `networkx.draw`                              | - Static network graph visualization<br>- Color nodes/edges by attributes | Intuitive understanding of network structures<br>Overview of observation relationships |
| 🔵 Medium      | **Data Visualization**   | `plotly`, `folium`, `geopandas`                            | - Interactive network visualization<br>- Mapping observation points on a map  | Understand spatial distribution<br>Visually link relationships with environmental data |
| 🔵 Medium      | **Network Analysis**     | `networkx`, `community`, `igraph`                          | - Node centrality & community detection<br>- Modularity & connectivity analysis | Identify key species/groups in networks<br>Deepen understanding of complex ecosystems |
| 🔵 Medium      | **Spatial Analysis**     | `pysal`, `scipy.spatial`                                   | - Spatial autocorrelation (Moran’s I)<br>- Spatial clustering         | Detect biodiversity hotspots and distribution patterns<br>Inform conservation & management decisions |
| 🔴 High        | **Multilayer Networks**  | `networkx.MultiGraph`, `multinetx`, `igraph`               | - Integrate with fungal networks<br>- Compare & merge multilayer networks | Visualize relationships across different ecological layers<br>Understand complex systems as networks |
| 🔴 High        | **Dynamic Network Analysis** | `matplotlib.animation`, `plotly`, `tulip`                  | - Visualize seasonal/time-series changes in networks<br>- Compute dynamic metrics like time-based centrality | Track temporal changes in species interactions & environmental responses<br>Build ecosystem dynamics models |
| 🔴 High        | **Environmental Data Prediction** | `scikit-learn`, `xgboost`, `lightgbm`, `pandas`            | - Machine learning models for soil fauna distribution<br>- Correlation & prediction with environmental factors | Predict soil fauna networks from environmental conditions<br>Apply to conservation and adaptive scenarios |

---

## 📌 Data Notes

* Species names, roles, and interactions are mock data based on real soil ecology
* Japanese labels are rendered with Meiryo and white stroke for legibility

Pull requests, forks, and fungi-fauna mashups welcome! 🌱

**Tags:** `#network-thinking` `#soil-fauna` `#complexity` `#ecology` `#from-RDB-to-network` `#mvp`
