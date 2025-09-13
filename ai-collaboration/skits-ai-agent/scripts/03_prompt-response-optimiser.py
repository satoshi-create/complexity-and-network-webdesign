from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# LLMモデル定義
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# スージョ風 Prompt Optimiser
optimiser_prompt = PromptTemplate(
    input_variables=["vague_request"],
    template="""
あなたは「スージョ」という構文研究をしている女子大生です。
深夜のファミレスでバイトをしながら、お客さんの曖昧な注文を
「構文的に分解」して、最後には自然な注文文に最適化します。

回答スタイル：
1. 「はい出ました、“○○構文”。」と命名
2. 要素分解（トーン、状態、希望内容）
3. 「👉 明確化された依頼：◯◯」と自然な注文文を提示

ユーザーの依頼: {vague_request}

スージョの最適化回答:
"""
)

# チェーン構築
optimiser_chain = LLMChain(llm=llm, prompt=optimiser_prompt)

# テスト入力
vague_input = "あの…なんか…あれで…"
clear_request = optimiser_chain.run(vague_input)

print("🔹 明確化結果:", clear_request)
