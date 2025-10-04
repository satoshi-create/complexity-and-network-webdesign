# ローカル
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY") # LangSmith 連携用
os.environ["LANGCHAIN_TRACING_V2"] = "true" # トレース有効化
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# google-colab
from google.colab import userdata
import os

# サイドバーで追加したシークレットを取得
apikey = userdata.get("OPENAI_API_KEY")

# 改行や空白を除去して環境変数に登録
if apikey:
    os.environ["OPENAI_API_KEY"] = apikey.strip()
else:
    raise ValueError("ColabのSecretsに OPENAI_API_KEY が設定されていません")
