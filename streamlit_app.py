import os
import streamlit as st
from mistralai import Mistral

st.set_page_config(page_title="Mistral AI Chat", page_icon="🤖")

# Read API key from environment
API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    st.error("MISTRAL_API_KEY not set. Please set it in your environment or Streamlit secrets.")
    st.stop()

client = Mistral(api_key=API_KEY)

# Sidebar settings
st.sidebar.title("Settings")
model = st.sidebar.selectbox("Model", ["mistral-large-latest"], index=0)
if st.sidebar.button("Clear conversation"):
    st.session_state.pop("history", None)

# Initialize session conversation
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Mistral AI Chat")
st.write("A simple web chat UI for your Mistral-powered bot.")

# Show chat history
for msg in st.session_state.history:
    role = msg.get("role")
    content = msg.get("content")
    if role == "user":
        st.markdown(f"**You:** {content}")
    else:
        st.markdown(f"**Bot:** {content}")

# Input area
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:")
    submit = st.form_submit_button("Send")

if submit and user_input:
    # Append user message
    st.session_state.history.append({"role": "user", "content": user_input})
    # Call Mistral
    try:
        response = client.chat.complete(
            model=model,
            messages=st.session_state.history,
            max_tokens=512
        )
        assistant_message = response.choices[0].message.content
    except Exception as e:
        assistant_message = f"Error: {e}"

    # Append assistant message and rerun
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    st.experimental_rerun()
