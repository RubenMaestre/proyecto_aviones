# modules/botones_eda.py
import streamlit as st

def crear_botones_eda():
    # Primera fila para los años y subpáginas
    st.write("Seleccione el año o subpágina:")
    row1_space1, row1_col1, row1_col2, row1_col3, row1_col4, row1_col5, row1_col6, row1_space2 = st.columns([1, 2, 2, 2, 2, 2, 2, 1])
    
    with row1_col1:
        if st.button("2023 - Parte 1", key="2023_btn"):
            st.session_state.subpagina_eda = "2023"
    
    with row1_col2:
        if st.button("2023 - Parte 2", key="2023_2_btn"):
            st.session_state.subpagina_eda = "2023_2"

    with row1_col3:
        if st.button("2022 - Parte 1", key="2022_btn"):
            st.session_state.subpagina_eda = "2022"

    with row1_col4:
        if st.button("2022 - Parte 2", key="2022_2_btn"):
            st.session_state.subpagina_eda = "2022_2"
    
    with row1_col5:
        if st.button("2021 - Parte 1", key="2021_btn"):
            st.session_state.subpagina_eda = "2021"

    with row1_col6:
        if st.button("2021 - Parte 2", key="2021_2_btn"):
            st.session_state.subpagina_eda = "2021_2"
    
    # Espacio entre filas
    st.write("---")
    
    # Segunda fila para las páginas "Todos"
    st.write("Visualización general:")
    row2_space1, row2_col1, row2_col2, row2_col3, row2_col4, row2_space2 = st.columns([1, 2, 2, 2, 2, 1])
    
    with row2_col1:
        if st.button("Todos - Página 1", key="todos_1_btn"):
            st.session_state.subpagina_eda = "todos_1"
    
    with row2_col2:
        if st.button("Todos - Página 2", key="todos_2_btn"):
            st.session_state.subpagina_eda = "todos_2"
    
    with row2_col3:
        if st.button("Todos - Página 3", key="todos_3_btn"):
            st.session_state.subpagina_eda = "todos_3"

    with row2_col4:
        if st.button("Todos - Página 4", key="todos_4_btn"):
            st.session_state.subpagina_eda = "todos_4"
