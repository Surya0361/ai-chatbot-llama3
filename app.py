import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Chatbot Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chatbot Assistant")
st.caption("Powered by Llama3 running locally with Ollama")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("Model: Llama3")
    st.write("Runs locally using Ollama")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    response = ollama.chat(
        model="llama3",
        messages=st.session_state.messages
    )

    reply = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)