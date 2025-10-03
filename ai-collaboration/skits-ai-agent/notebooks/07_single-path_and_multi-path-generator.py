# ===========================================
# step1: 必要なライブラリのインポート
# ===========================================
# ※事前に以下のコマンドでライブラリをインストールしてください
# pip install langchain openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


# ===========================================
# step2: モデル準備
# ===========================================
# OpenAI APIを利用したチャットモデルを呼び出し
# temperature=0 → 再現性のある一本道（Single-Path）に向く
# temperatureを上げると候補の幅（Multi-Path）が広がる

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# ===========================================
# step3: Single-Path Plan Generator
# ===========================================
# 寸劇で「一本道の温泉プラン」を提示したAI
# → ユーザーの要望に対し、最適と思うプランだけを返す

single_prompt = ChatPromptTemplate.from_template(
    "あなたは旅行プランナーです。"
    "ユーザの要望に対し、最適と思う一本道の計画だけを提案してください。\n"
    "要望: {request}"
)

single_chain = LLMChain(llm=llm, prompt=single_prompt)

request = "卒業旅行で箱根を楽しみたい"
single_result = single_chain.run({"request": request})
print("=== Single-Path Plan ===")
print(single_result)


# ===========================================
# step4: Multi-Path Plan Generator
# ===========================================
# 寸劇で「候補を複数提示」したAI
# → 複数の異なるプランを返す

multi_prompt = ChatPromptTemplate.from_template(
    "あなたは旅行プランナーです。"
    "ユーザの要望に対し、3〜4種類の異なるプランを提案してください。\n"
    "要望: {request}"
)

multi_chain = LLMChain(llm=llm, prompt=multi_prompt)

multi_result = multi_chain.run({"request": request})
print("\n=== Multi-Path Plan ===")
print(multi_result)


# ===========================================
# step5: まとめ
# ===========================================
# Single-Path → 「迷わず即決」
# Multi-Path → 「選んで合意形成」
# 寸劇のセツコ（選択肢大好き）とフォーム女子（一本道安心）の掛け合いを
# コードで再現して学べる流れ

print("\n寸劇で学んだ通り、SingleとMultiを状況に応じて使い分けましょう！")
