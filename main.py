import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title("👩🏻‍🔬 阴阳怪气小助手")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "？""您...有事吗"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("小助手正在皱眉思索..."):
        response = get_chat_response(prompt, st.session_state["memory"])
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
