from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool

# ゴールを記録するシンプルツール
goals = []
def write_goal(goal: str) -> str:
    goals.append(goal)
    return f"ゴールを記録しました: {goal}"

tools = [Tool(name="write_goal", func=write_goal, description="ゴールを記録する")]

llm = ChatOpenAI(model="gpt-4o-mini")

agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("昭和UXパーティーを開催せよ！"))
print(agent.run("まずは日時を決めて"))
print(agent.run("次に招待客リストを作れ"))

print("記録されたゴール:", goals)
