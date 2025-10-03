
pip install --upgrade langchain langchain-openai langgraph pydantic python-dotenv


from google.colab import userdata
import os

# サイドバーで追加したシークレットを取得
apikey = userdata.get("OPENAI_API_KEY")

# 改行や空白を除去して環境変数に登録
if apikey:
    os.environ["OPENAI_API_KEY"] = apikey.strip()
else:
    raise ValueError("ColabのSecretsに OPENAI_API_KEY が設定されていません")


# Step 1: 必要ライブラリのインポート
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI



# Step 2: LLMの初期化
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


# Step 3: Proactive Goal Creator のプロンプト定義
# ユーザーの依頼が曖昧でも、AIが「潜在的に必要なゴール」を3つ提案します。

template = """あなたは Proactive Goal Creator です。
ユーザーの依頼が曖昧な場合、潜在的に必要となるゴールを3つ提案してください。

ユーザー依頼: {request}
"""

prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: 実行してみる
# 例: 「新規事業のアイデアを出して」という曖昧な依頼を投げます。
request = "新規事業のアイデアを出して"
result = chain.run(request)
print("🔮 Proactive Goal Creator の提案:\n")
print(result)

# ✅ このように曖昧な依頼をすると、AIが「市場調査」「ユーザーインタビュー」「試作品テスト」などの
# ゴール候補を自動的に生成します。
# これが Proactive Goal Creator の基本的な流れです。
