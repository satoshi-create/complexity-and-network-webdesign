!pip install --upgrade langchain langchain-openai langgraph pydantic python-dotenv

from google.colab import userdata
import os

# サイドバーで追加したシークレットを取得
apikey = userdata.get("OPENAI_API_KEY")

# 改行や空白を除去して環境変数に登録
if apikey:
    os.environ["OPENAI_API_KEY"] = apikey.strip()
else:
    raise ValueError("ColabのSecretsに OPENAI_API_KEY が設定されていません")


# === ステップ2: 必要なモジュールを読み込む ===
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI


# === ステップ3: LLM（大規模言語モデル）の定義 ===
# 低コスト・高速試験用には gpt-4o-mini を推奨
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

optimiser_prompt = PromptTemplate(
    input_variables=["vague_request"],
    template="""
あなたは「スージョ」という構文研究をしている女子大生です。
深夜のファミレスでバイトをしながら、お客さんの曖昧な注文を
「構文的に分解」して、最後には自然な注文文に最適化します。

回答スタイル：
1. 「はい出ました、“○○構文”。」と構文名を命名する
2. 曖昧な依頼を「要素」に分解する（例：トーン、状態、希望内容）
3. その要素を組み合わせて、実際に通じる注文文を生成する
   → 「👉 明確化された依頼：◯◯」の形で提示する

シチュエーション：
- 舞台は深夜のファミレス
- 相手は疲れたサラリーマン（さと）
- あなたはエプロン姿で、ミニメモ帳に書きながら答える

ユーザーの依頼: {vague_request}

スージョの最適化回答:
"""
)


# === ステップ5: Optimiserチェーンの構築 ===
# LLMとプロンプトテンプレートを結合してチェーンを作成
optimiser_chain = LLMChain(llm=llm, prompt=optimiser_prompt)


# === ステップ6: 曖昧な依頼を入力し、明確化結果を確認 ===

# 例：寸劇の「さと」のセリフを入力
vague_input = "あの…なんか…あれで…"

# Optimiserを実行
clear_request = optimiser_chain.run(vague_input)

# 出力を表示
print("🔹 明確化結果:", clear_request)
