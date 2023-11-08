from openai import OpenAI
import streamlit as st
import time

st.set_page_config(
   page_title="您好世界",
   page_icon="🧊"
)

client = OpenAI(
    api_key = st.secrets["APP_KEY"]
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    message_placeholder = st.empty()
    full_response = ""
    assistant_response = '您好，我是您的AI助手，使用GPT3.5提供服务，您可以向我提问任何问题~'
    for chunk in assistant_response:
        full_response += chunk + " "
        time.sleep(0.01)
        message_placeholder.markdown(full_response + "_")
    message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input(""):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            res_tmp = response.choices[0].delta.content
            if res_tmp:
                full_response += res_tmp
            message_placeholder.markdown(full_response + "_")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})