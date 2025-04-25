graph TD
  A[第3層：枯草マルチ] --> B[第2層：播種＋微生物活性層]
  B --> C[第1層：耕起表土＋地下茎層]
  C --> D[地中層：団粒構造ゾーン]

  A:::mulch
  B:::biolayer
  C:::tillage
  D:::soilcore

  subgraph 作物
    E1[🌽 トウモロコシ（30cm間隔）] 
    E2[🥕 ダイコン（25cm間隔）] 
    E1 --> B
    E2 --> B
  end

  subgraph 生物ネットワーク
    F1[🕷️ スピグモ姐さん（コモリグモ）]
    F2[🪱 ミミズ長老]
    F3[🦗 ヨト丸（ヨトウムシ）]
    F4[🧫 キノコ菌糸（未同定）]
    F1 --> A
    F2 --> D
    F3 --> B
    F4 --> C
  end

