<p align="center">
  <img src="https://github.com/satoshi-create/complexity-and-network-webdesign/blob/main/docs/branding-mvp-launch/images/logos/logo_cultural-emergent.png" alt="CANW Logo" width="100"/>
</p>

<h1 align="center">🌐 CivicCommonsLab</h1>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Part of CANW](https://img.shields.io/badge/CANW-ecosystem-blueviolet)](https://github.com/satoshi-create/complexity-and-network-webdesign)
[![Wiki](https://img.shields.io/badge/Wiki-Explore%20More-blue)](https://github.com/satoshi-create/complexity-and-network-webdesign/wiki)
![Contributors](https://img.shields.io/github/contributors/satoshi-create/complexity-and-network-webdesign?color=brightgreen)

📘 Read in other languages:

- [🇯🇵 Japanese](./README_ja.md)

> CivicCommonsLab: rethinking local government data as living commons.

This project is part of **CANW** (Complexity And Network Webdesign).
For the broader vision and conceptual architecture of CANW, please refer to the [root README](https://github.com/satoshi-create/complexity-and-network-webdesign).

---

## 🔄 Overview: CivicCommonsLab

**CivicCommonsLab** is an experimental project that reimagines local government documents as **commons of daily life**.
We aim to transform rigid administrative data (like waste sorting PDFs) into structures that reflect the **lived world (Umwelt)** of citizens, making them more accessible, interconnected, and meaningful.

---

## 🧪 Current Focus: Machida Gomi Structure

Our first prototype, [**machida-gomi-structure**](./machida-gomi-structure), takes the waste sorting PDF of Machida City as a starting point.
We extract text via OCR, classify and normalize it, and export it as structured data (CSV/JSON).
Using **Mermaid.js** and **NetworkX**, we visualize the classification logic, highlighting hidden relationships in the administrative environment.

---

## 🛠 Tech Stack & Collaboration

We employ:

- Python (OCR, pandas, JSON/CSV export)
- Mermaid.js, NetworkX for visualization
- Jupyter Notebook for AI–human co-creation

We emphasize:

- Complexity as structure, not noise
- Human × AI collaboration to reveal the underlying "story"
- UX as a bridge between institutional systems and lived experiences

📎 GitHub repository:
[https://github.com/satoshi-create/civic-commons-lab](https://github.com/satoshi-create/civic-commons-lab)

---

## 🌐 Ecosystem Flow (Mermaid)

```mermaid
graph TD
  A[Local Government PDFs] --> B[OCR & Text Normalization]
  B --> C[Categorization & Structure]
  C --> D[Visualization (Mermaid.js, NetworkX)]
  D --> E[Reflection & UX Storytelling]
  E --> F[Integration with CANW]

  subgraph Prototypes
    P1[machida-gomi-structure]
  end

  C --> P1
```
