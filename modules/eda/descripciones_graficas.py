# modules/eda/descripciones_graficas.py
import streamlit as st
import pandas as pd

@st.cache
def cargar_descripciones():
    return pd.read_excel('data/graficas/comentarios.xlsx')

def obtener_descripcion(year, grafica_seleccionada, descripciones):
    # Asegúrate de que 'year' sea un string si los años en Excel están como texto
    year = str(year)
    try:
        filtro = ((descripciones['years'] == year) | (descripciones['years'] == 'Todo')) & (descripciones['grafica'] == grafica_seleccionada)
        descripcion = descripciones[filtro]['comentario'].iloc[0] if any(filtro) else "Descripción no disponible."
    except Exception as e:
        descripcion = f"Error al obtener descripción: {str(e)}"
    return descripcion
