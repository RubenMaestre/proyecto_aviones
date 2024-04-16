#paginas/modelo.py
import streamlit as st
from modules.ml.ml_2 import display_ml_page

def display():
    st.title('Modelo machine learning')
    # Aquí iría el resto de tu contenido de la página de inicio

    st.markdown("""
    Haz tu selección para saber si tu vuelo llegará con retraso o no con nuestro infalible modelo de prediccón...
    """)
    display_ml_page()