# =========================================================
# Reflection デモコード (Self → Cross → Human)
# =========================================================


# このコードは VSCode などで .py として実行できます。
# 事前に OpenAI API キーを環境変数 OPENAI_API_KEY に設定してください。
pip install langchain openai
# =========================================================

from google.colab import userdata
import os

# サイドバーで追加したシークレットを取得
apikey = userdata.get("OPENAI_API_KEY")

# 改行や空白を除去して環境変数に登録
if apikey:
    os.environ["OPENAI_API_KEY"] = apikey.strip()
else:
    raise ValueError("ColabのSecretsに OPENAI_API_KEY が設定されていません")



from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI


# =========================================================
# 0. 準備
# =========================================================
# OpenAI LLM のインスタンス生成
llm = OpenAI(temperature=0.3)

# 最初の句
initial_sentence = "古地図に コンテクスト咲く 冬の道"


# =========================================================
# 1. Self-Reflection（俳句的反省）
# =========================================================
self_prompt = PromptTemplate(
    input_variables=["sentence"],
    template="""
句: {sentence}

1. この句の良い点を述べてください。
2. 改善点を指摘してください。
3. 改善を踏まえて改稿句を提示してください。
"""
)

self_chain = LLMChain(llm=llm, prompt=self_prompt)
self_result = self_chain.run(sentence=initial_sentence)

print("=== Self-Reflection ===")
print(self_result)


# =========================================================
# 2. Cross-Reflection（連句的批評）
# =========================================================
cross_prompt = PromptTemplate(
    input_variables=["sentence"],
    template="""
あなたは句会に参加するAIです。
仲間の句を読んで、批評を与えてください。

句: {sentence}

- 批評コメント
- 改善提案
"""
)

cross_chain = LLMChain(llm=llm, prompt=cross_prompt)

# Self-Reflection での改稿句を仮定（寸劇の流れに沿って例を設定）
sentence_from_self = "雪の駅 風と落書き 旅の跡"
cross_result = cross_chain.run(sentence=sentence_from_self)

print("\n=== Cross-Reflection ===")
print(cross_result)


# =========================================================
# 3. Human Reflection（読者の座）
# =========================================================
human_prompt = PromptTemplate(
    input_variables=["sentence", "feedback"],
    template="""
元の句:
{sentence}

人間の読者からのフィードバック:
{feedback}

このフィードバックを踏まえて、句を改稿してください。
"""
)

human_chain = LLMChain(llm=llm, prompt=human_prompt)

# 芭蕉（人間読者）のフィードバックを例示
feedback = "『attention』という表現は抽象的です。より具体的に『視線』と表現してください。"
human_result = human_chain.run(
    sentence="雪の道 attention灯る 無人駅",
    feedback=feedback
)

print("\n=== Human Reflection ===")
print(human_result)


# =========================================================
# End
# =========================================================
print("\n=== 完了 ===")
