import openai
import streamlit as st

st.title("Marcar consulta")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state: 
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state["messages"] = []



for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Fale sobre sua consulta"):
    instructions = (
    "Você é um assistente virtual de uma clínica médica, responsável por agendar consultas. "
    "Sempre seja educado, objetivo e profissional. "
    "Ao iniciar a conversa, cumprimente o paciente e pergunte se deseja marcar uma consulta. "
    "Se ele responder afirmativamente, peça informações como plano de saúde, data e local desejado. "
    "Se o plano for Notredame, informe que ele não é aceito. Caso contrário, ofereça a opção de consulta particular. "
    "Evite repetir perguntas já respondidas pelo paciente e confirme todos os detalhes no final da conversa. "
    "Nunca peça informações irrelevantes e mantenha um tom profissional e acolhedor."
)

    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        client = openai.OpenAI()  
        stream = client.chat.completions.create(
            model=st.session_state['openai_model'],
           messages=[
    {"role": "system", "content": instructions}
] + st.session_state["messages"] + [{"role": "user", "content": prompt}]
,
            stream=True
        )
        response = st.write_stream(stream)
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
