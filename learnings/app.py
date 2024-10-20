# sample app
import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there Aida",
            "Hello whats ups Lorna",
            "Hello good day Fe"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title('Simple Chat Sample App')

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on app rerun
for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"
#Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
#add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})





