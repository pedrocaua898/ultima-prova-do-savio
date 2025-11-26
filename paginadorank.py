import streamlit as st

# isso garante q o rank vai ficar salvo
if "ranks" not in st.session_state:
    st.session_state.ranks = []

def add_to_ranking(nome, tema, dificuldade, pontos):
    st.session_state.ranks.append({
        "nome": nome,
        "tema": tema,
        "dificuldade": dificuldade,
        "pontos": pontos
    })

def render_ranking():
    st.title("🏆 Ranking Geral")

    if len(st.session_state.ranks) == 0:
        st.info("Nenhum registro ainda.")
        return

    ordenado = sorted(st.session_state.ranks, key=lambda x: x["pontos"], reverse=True)

    for i, r in enumerate(ordenado):
        st.write(f"""
### {i+1}º — {r['nome']}
- Tema: **{r['tema']}**
- Dificuldade: **{r['dificuldade']}**
- Pontos: **{r['pontos']}**
""")

    st.divider()

    if st.button("Voltar"):
        st.session_state.pagina = "welcome"
        st.rerun()
