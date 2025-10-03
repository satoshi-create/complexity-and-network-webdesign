# Converted from 06_incremental-model-querying.ipynb

# ===============================# Code cell# ===============================
pip install --upgrade langchain langchain-openai langgraph pydantic python-dotenv faiss-cpu

# ===============================# Code cell# ===============================
pip install -U langchain-community

# ===============================# Code cell# ===============================
from google.colab import userdata
import os

# サイドバーで追加したシークレットを取得
apikey = userdata.get("OPENAI_API_KEY")

# 改行や空白を除去して環境変数に登録
if apikey:
    os.environ["OPENAI_API_KEY"] = apikey.strip()
else:
    raise ValueError("ColabのSecretsに OPENAI_API_KEY が設定されていません")


# ===============================# Code cell# ===============================
# ===============================
# セル1: 必要ライブラリのインポート
# ===============================

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


# ===============================# Code cell# ===============================
# ===============================
# セル2: モデルの初期化
# ===============================
# ここでは gpt-4o-mini を例に使用
# （環境によって "gpt-4o-mini" → "gpt-4" などに変更可能）

llm = ChatOpenAI(model="gpt-4o-mini")


# ===============================# Code cell# ===============================
# ===============================
# セル3: Incremental Query の準備
# ===============================
# ミャクミャケがもやもやして投げたいテーマを「小分け」に分解する

questions = [
    "行政手続きにおける『紙の手続き』のメリットを3つ挙げてください。",
    "行政手続きにおける『デジタル手続き』のメリットを3つ挙げてください。",
    "紙とデジタルの両方を共存させる方法を提案してください。"
]


# ===============================# Code cell# ===============================
# ===============================
# セル4: 段階的に問い合わせる
# ===============================
# 1問ずつモデルに投げて、回答を蓄積していく

answers = []

for idx, q in enumerate(questions, 1):
    response = llm([HumanMessage(content=q)])
    print(f"Q{idx}: {q}")
    print("A:", response.content, "\n")
    answers.append(response.content)


# ===============================# Code cell# ===============================
# ===============================
# セル5: 最後にまとめを依頼
# ===============================
# これまでの回答を統合して、ハイブリッド戦略を要約

summary_prompt = "以下の回答を統合して、行政手続きの簡素化戦略を提案してください:\n\n"
summary_prompt += "\n".join(answers)

final_summary = llm([HumanMessage(content=summary_prompt)])
print("=== 最終まとめ ===")
print(final_summary.content)
