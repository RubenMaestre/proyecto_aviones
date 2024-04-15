import streamlit as st
from modules.categoria_graficas import get_graficas_por_categoria


def seleccionar_grafica():
    categorias = get_graficas_por_categoria()
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", list(categorias.keys()))
    graficas = categorias[categoria_seleccionada]
    grafica_seleccionada = st.selectbox("Selecciona una gráfica para visualizar:", list(graficas.keys()))
    return graficas[grafica_seleccionada]


