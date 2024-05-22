import streamlit as st
# import cohere
from chatbot import ChatBot, SYSTEM_MESSAGE_PROMPT

# # get cohere api key from .env
# from dotenv import load_dotenv
# import os

# load_dotenv()

# COHERE_API_KEY = os.getenv("COHERE_API_KEY")
# CREATIVITY = 0

# uploaded_files = st.sidebar.file_uploader("Upload image", type=['png', 'jpg', 'pdf'], accept_multiple_files=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "user",
            "message": SYSTEM_MESSAGE_PROMPT,
        },
        {
            "role": "assistant",
            "message": "Hello, I'm a chatbot built to help you query OECD test guidelines."
        },
    ]


st.title("Repro-Tox Demo")

st.session_state.bot = ChatBot()

if "cohere_model" not in st.session_state:
    st.session_state["cohere_model"] = "command"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])

if prompt := st.chat_input("Text here..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = st.session_state.bot.query(
            prompt,
            chat_history=st.session_state.messages,
            message_placeholder=message_placeholder
        )
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "user", "message": prompt})
    st.session_state.messages.append({"role": "assistant", "message": full_response})