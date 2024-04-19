import streamlit as st
import pandas as pd

# Cargar las descripciones desde Excel
@st.cache  # Usando @st.cache estándar
def cargar_descripciones():
    return pd.read_excel('data/graficas/comentarios.xlsx')

descripciones = cargar_descripciones()

# Función para obtener la descripción basada en el año y la gráfica seleccionada
def obtener_descripcion(year, grafica_seleccionada):
    # Asegúrate de que 'year' sea un string si los años en Excel están como texto
    year = str(year)
    filtro = ((descripciones['years'] == year) | (descripciones['years'] == 'Todo')) & (descripciones['grafica'] == grafica_seleccionada)
    descripcion = descripciones[filtro]['comentario'].iloc[0] if any(filtro) else "Descripción no disponible."
    return descripcion
