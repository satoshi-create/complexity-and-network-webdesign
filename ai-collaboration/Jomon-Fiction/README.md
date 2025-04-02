# Jomon Fiction – AIと協働して描く縄文の物語  
**Jomon Fiction – Reimagining the Jomon World Through AI Collaboration**

---

## 🤝 概要 | Overview

「Jomon Fiction」は、**AI と人間が協働して縄文時代の景観ランドスケープを立ち上げるプロジェクト**です。
本プロジェクトは、「複雑系とネットワークのウェブデザイン（CANW）」の中の [`ai-collaboration`](../) サブプロジェクトとして位置づけられています。

**Jomon Fiction** is a collaborative storytelling project where humans and AI co-create imaginative narratives set in the Jomon period of prehistoric Japan.  
It is part of the [`ai-collaboration`](../) subproject within the **CANW (Complexity and Network-based Web Design)** initiative.


---

## 🧭 目的と背景 | Purpose and Vision

本プロジェクトでは、**忠生遺跡・阿久遺跡・下野谷遺跡**などの**拠点的集落**をテーマに、  
ネットワーク・環境・信仰・暮らしといった複数の視点から小説を構築します。

The project focuses on key Jomon settlements such as **Tadao, Aku, and Shimonoya**.  
Each narrative explores these sites through the lenses of **networks, environment, belief systems, and daily life**.

---

## 🤖 AIとの協働 | Working with AI

本プロジェクトでは、以下のようにAIがクリエイティブプロセスに参加します：

| 工程 | 人間の役割 | AIの役割 |
|------|------------|----------|
| 構想・調査 | 土地選定・視点設計・文脈把握 | 類例生成・構造提案・メタ的思考補助 |
| 物語制作 | プロット構築・物語の声を決める | スタイル提案・構文補正・翻訳支援 |
| 可視化 | ネットワーク構築・図解の構想 | Pythonによる可視化コード・出力整形 |
| 図像制作 | 構図と質感の設計 | DALL·E等による画像生成 |

In this project, AI acts as a **creative partner** in the following stages:

| Phase | Human Role | AI Role |
|-------|------------|---------|
| Conceptualization | Selecting sites, perspectives, and contexts | Generating patterns, offering structural suggestions |
| Writing | Designing plots, narrative tone and characters | Style assistance, syntax feedback, bilingual translation |
| Visualization | Designing networks and diagrams | Python code for graph generation, image formatting |
| Image Creation | Planning visual themes and texture | Generating illustrations via DALL·E or similar tools |

---

## 📁 ディレクトリ構成 | Directory structure

```plaintext
jomon-fiction/
├── README.md
├── index.md
├── sites/
│   ├── tadao/
│   │   ├── story_ja.md         ← 忠生遺跡物語（日本語）
│   │   ├── story_en.md         ← Tadao story (English)
│   │   ├── network.ipynb       ← ネットワーク図生成（Jupyter）
│   │   └── images/
│   │       └── landscape.png
│   ├── aku/
│   │   └── ...
│   └── shimonoya/
│       └── ...
├── common-assets/
│   └── css, fonts, templates
├── characters/

```



※ 日本語と英語は**同一ディレクトリ内に併記**し、翻訳ではなく**文化的再構成**として扱います。

---

## 🌐 発信と公開 | Publishing & Outreach

- note連載（予定）:
- CANWウェブサイトとの連携を予定  
- 生成物（物語、図像、ネットワーク図など）はOSSとして公開予定

This project will be shared via:
- Serialized posts on note.com 
- Integration with the CANW website  
- Open-source publication of all stories, images, and networks

---

## 🚧 現在進行中 | Work in Progress

- [x] README bilingual draft  
- [ ] 忠生遺跡編 プロット執筆中  
- [ ] obsidian/shell trade ネットワーク構造のモデリング  
- [ ] note連載（2025年4月公開予定）

---
