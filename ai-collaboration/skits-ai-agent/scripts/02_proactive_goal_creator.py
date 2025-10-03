from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

template = """あなたは Proactive Goal Creator です。
ユーザーの依頼が曖昧な場合、潜在的に必要となるゴールを3つ提案してください。

ユーザー依頼: {request}
"""
prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("新規事業のアイデアを出して"))
