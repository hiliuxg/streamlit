from openai import OpenAI
import streamlit as st
import extra_streamlit_components as stx
from chat_history import ChatHistory


def get_chat_history():
    return ChatHistory()

chat_history = get_chat_history()

def chat_his_item_calback(parmas):
    st.write(parmas)

with st.sidebar:


    if "chat_his_del_checking" not in st.session_state:
        st.session_state["chat_his_del_checking"] = False

    col1, col2 = st.columns(spec = [0.7, 0.3])

    with col1:
        bt_add = st.button("添加新的聊天", type="primary", use_container_width=True)
        if bt_add:
            chat_history.add_item(topic = "今天流行去趋势")

    with col2:
        bt_del = st.button("删除", type="secondary", use_container_width=True)
        if bt_del and st.session_state["chat_his_del_checking"]:
            st.session_state["chat_his_del_checking"] = False
        elif bt_del and st.session_state["chat_his_del_checking"] == False:
            st.session_state["chat_his_del_checking"] = True

    list_chat_history = chat_history.list_items()
    if st.session_state["chat_his_del_checking"]:
        for idx, item in enumerate(list_chat_history[::-1]):
            st.checkbox(item['topic'], key = idx)
    else:
        st.radio(":gray[历史聊天会话]", 
                 index=None,
                 options = list_chat_history[::-1], 
                 format_func=lambda x: x['topic'])
        
      
    