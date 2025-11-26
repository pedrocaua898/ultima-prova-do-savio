import streamlit as st
from paginadoquiz import render_quiz

def render_welcome():
    st.image("logo.png", width=200)   # isso aq serve pra colocar aquela logo q tu fez no canva dudu
    st.title("📘 Quiz Educacional NEP")

def render_welcome():

    st.title("📘 Quiz Educacional NEP")
    st.write("### Bem-vindo! Escolha o tema e a dificuldade para começar seu quiz.")

    st.divider()

    nome = st.text_input("👤 Seu nome:", placeholder="Digite seu nome aqui") #nome do caba q vai fazer o teste

    st.write("### 🎯 Escolha um tema:")
    tema = st.radio(
        "",
        ["Matemática", "Português", "Geografia"],
        horizontal=True
    )

    st.write("### ⚡ Selecione a dificuldade:")
    dificuldade = st.radio(
        "",
        ["Fácil", "Médio", "Difícil"],
        horizontal=True
    )

    st.divider()

    iniciar = st.button("▶ Iniciar Quiz", use_container_width=True)

    if iniciar:
        if nome.strip() == "":
            st.warning("⚠ Por favor, digite seu nome antes de iniciar.")
        else:
            render_quiz(tema, dificuldade, nome)
