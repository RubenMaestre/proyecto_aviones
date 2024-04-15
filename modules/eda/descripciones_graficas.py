import streamlit as st
import pandas as pd

# Cargar las descripciones desde CSV
@st.cache
def cargar_descripciones():
    return pd.read_csv('data/graficas/comentarios.csv')

descripciones = cargar_descripciones()

# Función para obtener la descripción basada en el año y la gráfica seleccionada
def obtener_descripcion(año, grafica_seleccionada):
    filtro = (descripciones['año'] == año) & (descripciones['grafica'] == grafica_seleccionada)
    descripcion = descripciones[filtro]['descripcion'].iloc[0] if any(filtro) else "Descripción no disponible."
    return descripcion