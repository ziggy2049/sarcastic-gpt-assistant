from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
def get_chat_response(prompt, memory):
    # 定义带有阴阳怪气语气的系统提示词
    sarcastic_system_prompt = (
        "你是一个富贵公子哥，说话阴阳怪气、充满讽刺，对老板问的所有问题都带有一种挑衅的语气。"
    )

    # 创建带有系统提示的对话模板
    chat_prompt_template = ChatPromptTemplate.from_messages([
        ("system", sarcastic_system_prompt),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="sk-OalU6JpC0YTzmYciAb336dAcB8854dCcAc777499C991Df1f",
                       openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory, prompt=chat_prompt_template)

    response = chain.invoke({"input": prompt})
    return response["response"]

# 示例调用
memory = ConversationBufferMemory(return_messages=True)
print(get_chat_response("你觉得今天天气怎么样？", memory))