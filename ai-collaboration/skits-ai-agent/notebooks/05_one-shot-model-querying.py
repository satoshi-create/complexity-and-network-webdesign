
# ---------------- Step 1 ----------------
# 必要なライブラリをインストール（環境によっては不要）

pip install --upgrade langchain langchain-openai langgraph pydantic python-dotenv faiss-cpu

# ---------------- Step 2 ----------------
# LangChain Community パッケージ（必要な場合のみ）

pip install -U langchain-community

# ---------------- Step 3 ----------------
# APIキーの設定（Colab用記述は削除し、通常の環境変数利用を想定）
import os

# OpenAI APIキーを環境変数から取得
apikey = os.getenv("OPENAI_API_KEY")
if not apikey:
    raise ValueError("環境変数 OPENAI_API_KEY が設定されていません")
else:
    os.environ["OPENAI_API_KEY"] = apikey.strip()

# ---------------- Step 4 ----------------
# LangChainのOpenAIラッパーを利用
from langchain_openai import ChatOpenAI

# モデル準備
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ---------------- Step 5 ----------------
# 情報不足のプロンプト（失敗例）
prompt_bad = "ETCどう使うの？"
response_bad = llm.invoke(prompt_bad)

print("【失敗プロンプト】")
print(prompt_bad)
print("\n【ETC姉の回答】")
print(response_bad.content)

# ---------------- Step 6 ----------------
# 正しいプロンプト（成功例）
prompt_good = (
    "ETC初心者です。"
    "高速道路入口で使う方法を3ステップで説明してください。"
    "カードの入れ方・差し込み場所・注意点を含めて、100文字以内で簡潔に。"
)
response_good = llm.invoke(prompt_good)

print("\n==============================")
print("【成功プロンプト】")
print(prompt_good)
print("\n【ETC姉の回答】")
print(response_good.content)
