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


from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool


# --- LLM の設定 ---

llm = ChatOpenAI(model="gpt-4o-mini")


# --- ゴールを記録するシンプルなツール ---
goals = []

# def write_goal(goal: str) -> str:
#     goals.append(goal)
#     return f"ゴールを記録しました: {goal}"

def write_goal(goal: str) -> str:
    # ゴール文の最初の部分だけを残す（改行や句点で分割）
    short_goal = goal.split("。")[0].split("\n")[0]
    goals.append(short_goal)
    return f"ゴールを記録しました（要点）: {short_goal}"


tools = [
    Tool(
        name="write_goal",
        func=write_goal,
        # description="ゴールを記録し、タスクに分解する"
        description="ゴールを簡潔に記録する"
    )
]


# --- Passive Goal Creator エージェントを作成 ---
agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# --- 実行例 ---
print(agent.run("昭和UXパーティーを開催せよ！"))
print(agent.run("まずは日時を決めて"))
print(agent.run("次に招待客リストを作れ"))

# --- 要点だけのゴールを表示 ---
print("📌 要点ゴール一覧:", goals)

