import openai
import streamlit as st

st.title("ChatGPT like")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state: 
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("O que você quer saber hoje?"):
    instructions = "Responda as perguntas de maneira ágil"

    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        client = openai.OpenAI()  
        stream = client.chat.completions.create(
            model=st.session_state['openai_model'],
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        response = st.write_stream(stream)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
