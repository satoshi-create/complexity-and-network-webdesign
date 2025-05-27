# 🗑️ machida-gomi-structure

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Part of CivicCommonsLab](https://img.shields.io/badge/CivicCommonsLab-ecosystem-blueviolet)](../)

> A prototype for rethinking waste sorting data as living commons.

---

## 🔄 Project Overview

**machida-gomi-structure** is a sub-project within **CivicCommonsLab**.
It focuses on the waste sorting PDF from Machida City, aiming to transform it from static text into structured data (CSV/JSON) that better reflects the living environment of citizens.

By treating waste categories not just as rules but as **ecological and social structures**, this project invites us to see administrative data as part of our daily commons.

---

## 🛠️ MVP Workflow

1️⃣ **OCR & Text Extraction**
2️⃣ **Basic Normalization**
3️⃣ **Category Classification**
4️⃣ **Export as CSV/JSON**
5️⃣ **Visualization (Mermaid.js / NetworkX)**
6️⃣ **Storytelling & Reflection**

The goal is to make administrative data more accessible, interconnected, and meaningful — **without oversimplifying its inherent complexity**.

---

## ⚙️ Tech Stack

- **Python**: OCR, pandas, JSON/CSV output
- **Mermaid.js**: Flow diagrams
- **NetworkX**: Relationship network visualization

---

## 📂 Directories

```plaintext
machida-gomi-structure/
├── data/
│   ├── raw/            # Original PDF
│   ├── ocr_text/       # Extracted text
│   ├── csv/            # CSV output
│   └── json/           # JSON output
│
├── scripts/            # OCR, normalization, categorization, export scripts
├── visualization/      # Mermaid & NetworkX examples
├── README.md           # This file
└── .gitignore
```
