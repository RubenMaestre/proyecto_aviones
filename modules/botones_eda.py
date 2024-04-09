# modules/botones_eda.py
import streamlit as st

def crear_botones_eda():
    # Usamos st.columns para crear un diseño con espacios alrededor de los botones para centrarlos
    espacio_izq, col1, col2, col3, col4, espacio_der = st.columns([1, 2, 2, 2, 2, 1])

    with col1:
        if st.button("2023", key="2023_btn"):
            st.session_state.subpagina_eda = "2023"

    with col2:
        if st.button("2022", key="2022_btn"):
            st.session_state.subpagina_eda = "2022"

    with col3:
        if st.button("2021", key="2021_btn"):
            st.session_state.subpagina_eda = "2021"
    
    with col4:
        if st.button("Todos años", key="todos_btn"):
            st.session_state.subpagina_eda = "todos"
