import streamlit as st
from openai import AzureOpenAI
import os

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = AzureOpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                     api_version="2024-02-01",
                     azure_endpoint=os.getenv("OPENAI_ENDPOINT") )

model = os.getenv("OPENAI_MODEL")

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = model

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

# Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
