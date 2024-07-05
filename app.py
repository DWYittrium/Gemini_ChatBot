"""
1.type in terminal to install:
  - pip install google.generativeai
  - pip install streamlit
  
2.type the following in the terminal to use your api key:
  - setx GEMINI_API_KEY "your_api_key_here"
  
3.run by typing this into the terminal:
  - 
"""

import os
import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the GenerativeModel instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Streamlit UI
st.title("Simple Gemini ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send message to the chat session and get the response
    response = chat_session.send_message(prompt)
    assistant_response = chat_session.last.text

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
