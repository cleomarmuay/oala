import openai
import streamlit as st
import os
from streamlit_chat import message as msg

openai.api_key = "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"

st.title("Assistente Virtual OALA")

st.subheader("ChatBot-v.BETA")
st.subheader("Em que posso te Ajudar?")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = []

conversa = st.text_input("Digite a pegurta:")
btn_enviar_msg = st.button("Enviar Pergunta")
if btn_enviar_msg:
    st.session_state.hst_conversa.append({"role": "user", "content": conversa})
    retorno_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state.hst_conversa,
        max_tokens = 500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant",
                                          "content": retorno_openai['choices'][0]['message']['content']})

if len(st.session_state.hst_conversa) > 0:
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            msg("Você: " + st.session_state.hst_conversa[i]['content'], is_user=True)
        else:
            msg("OALA: " + st.session_state.hst_conversa[i]['content'])
