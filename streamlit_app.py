from openai import OpenAI
import streamlit as st
import time

st.set_page_config(
   page_title="您好世界~",
   page_icon="🧊"
)

client = OpenAI(
    #base_url = 'http://fxai.kugou.net/ai/proxy/openai/v1',
    api_key = st.secrets["APP_KEY"]
    #api_key = 'enDi7ZDdsKalxY6IDkMY+g=='
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
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
    prompt = prompt.replace('\n', '  \n')
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown('正在思考...')
        full_response = ""
        for response in client.chat.completions.create(
            model = st.session_state["openai_model"],
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages[-5:]
            ],
            stream=True
        ):
            res_tmp = response.choices[0].delta.content
            full_response += res_tmp if res_tmp is not None else ''
            message_placeholder.markdown(full_response + "_")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})