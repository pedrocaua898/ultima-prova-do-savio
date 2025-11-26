import streamlit as st
from questao import obter_questoes
from paginadorank import add_to_ranking

def render_quiz(tema, dificuldade, nome):

    st.header(f"📘 Quiz de {tema} — {dificuldade}")

    lista = obter_questoes(tema, dificuldade)

    respostas_usuario = []

    for i, q in enumerate(lista):
        st.write(f"### {i+1}) {q['pergunta']}")
        resposta = st.radio(
            "Escolha uma resposta:",
            q['opcoes'],        # ei nicolas, eu alterei a variável pq tava dando erro na hora de chamar a def
            key=f"pergunta_{i}"
        )
        respostas_usuario.append(resposta)
        st.divider()

    if st.button("Finalizar Quiz", use_container_width=True):
        pontos = 0
        st.subheader("📊 Resultado")

        for i, q in enumerate(lista):
            if respostas_usuario[i] == q["correta"]:    # alterei esse tbm, dps vou subir la no github pra atualizar bl
                pontos += 1
                st.success(f"✔ {q['pergunta']}")
            else:
                st.error(f"✘ {q['pergunta']} — Correta: **{q['correta']}**")

        st.info(f"🎉 Pontuação final: **{pontos}/{len(lista)}**")

        add_to_ranking(nome, tema, dificuldade, pontos)
