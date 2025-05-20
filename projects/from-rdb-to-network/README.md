<p align="center">
  <img src="https://github.com/satoshi-create/complexity-and-network-webdesign/blob/main/docs/branding-mvp-launch/images/logos/logo_cultural-emergent.png" alt="CANW Logo" width="100"/>
</p>

<h1 align="center">🌐 from-RDB-to-Network</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Part of CANW](https://img.shields.io/badge/CANW-ecosystem-blueviolet)](https://github.com/satoshi-create/complexity-and-network-webdesign)
[![Wiki](https://img.shields.io/badge/Wiki-Explore%20More-blue)](https://github.com/satoshi-create/complexity-and-network-webdesign/wiki)
![Contributors](https://img.shields.io/github/contributors/satoshi-create/complexity-and-network-webdesign?color=brightgreen)

[![#03_evolving-network-mvp_faminine_note.png](https://github.com/satoshi-create/complexity-and-network-webdesign/blob/main/docs/branding-mvp-launch/images/sns/03_rdb-to-network/%2303_evolving-network-mvp_faminine_note_en.png)]()

📘 Read in other languages:

* [🇯🇵 日本語](./README_ja.md)

> From rigid structures to living systems — a journey in rethinking data.
> 

This project is part of **CANW** (Complexity And Network Webdesign).
For the broader vision and conceptual architecture of CANW, please refer to the [root README](https://github.com/satoshi-create/complexity-and-network-webdesign).

---

## 🔄 Overview: From RDB to Network

**From RDB to Network** is an experimental project that transforms relational data into network graphs using Python (pandas + NetworkX).

Disparate CSVs and SQL tables are reconnected through the lens of **relationships**,
reconstructing data into a **web of interconnected meaning**.
The transformation process itself becomes a story — a shift from static records to living systems.

---

## 🧪 Current Prototypes

Within the CANW ecosystem, we are developing use-case prototypes such as:

* 🍄 **Fungi Network**

  * Modeling fungal hyphal structures from CSV data and visualizing their network dynamics
* ⚩ **Shrine Network**

  * Mapping shrines worshiping the same deity and visualizing their geographic and relational networks
* 🐜 **Soil Fauna Network**

  * Representing co-occurrence and predator-prey relations among soil organisms as ecological graphs

---

## 🛠 Tech Stack & OSS Approach

Currently, the pipeline is built using Python (pandas + NetworkX), with the following principles:

* Entities and relationships are defined in CSV format
* Node attributes and labeled edges enrich semantic context
* Layout emphasizes **spatial structures**, not random positioning

📎 GitHub repository:
[https://github.com/satoshi-create/from-rdb-to-network](https://github.com/satoshi-create/from-rdb-to-network)

---

## 🌐 Ecosystem Flow (Mermaid)

```mermaid
graph TD
  A[CSV / RDB Data Sources] --> B[Network Transformation_pandas + NetworkX]
  B --> C[Visualization_NetworkX / Neo4j / D3.js]
  C --> D[Frontend Rendering_Next.js / React / Canvas]
  D --> E[Reflection & Storytelling]
  E --> F[Integration with CANW Architecture]

  subgraph Prototypes
    P1[Fungi Network]
    P2[Shrine Network]
    P3[Soil Fauna Network]
  end

  subgraph Derivative Projects
    M1[Tobimushi Manga]
    M2[Jomon Fiction / Shrine Fiction]
  end

  B --> P1
  B --> P2
  B --> P3

  P1 --> M1
  P3 --> M1
  P2 --> M2

```

---

## 📄 License

This project is licensed under the MIT License.
See [LICENSE](./LICENSE) for details.

---

## 🔗 Related Links

* GitHub (From RDB to Network): [https://github.com/satoshi-create/complexity-and-network-webdesign/tree/main/projects/from-rdb-to-network](https://github.com/satoshi-create/complexity-and-network-webdesign/tree/main/projects/from-rdb-to-network)
* GitHub (CANW Main Repository): [https://github.com/satoshi-create/complexity-and-network-webdesign](https://github.com/satoshi-create/complexity-and-network-webdesign)
* LinkedIn (Global Outreach): [https://www.linkedin.com/in/satoprofile/](https://www.linkedin.com/in/satoprofile/)

---

**What is data?**
Let’s rethink its potential — from rigid structures to living networks.
