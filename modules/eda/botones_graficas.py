# modules/eda/botones_graficas.py
import streamlit as st
from modules.eda.categoria_graficas import get_graficas_por_categoria

def seleccionar_grafica():
    categorias = get_graficas_por_categoria()
    if categorias:
        categoria_seleccionada = st.selectbox("Selecciona una categoría:", list(categorias.keys()))
        graficas = categorias[categoria_seleccionada]
        grafica_seleccionada = st.selectbox("Selecciona una gráfica para visualizar:", list(graficas.keys()))
        # Devuelve la función gráfica y el nombre de la gráfica seleccionada
        return graficas[grafica_seleccionada], grafica_seleccionada
    else:
        st.write("No hay gráficas disponibles para este año.")
        return None, None