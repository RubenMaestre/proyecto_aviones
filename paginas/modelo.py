#paginas/modelo.py
import streamlit as st
from modules.ml.ml_1 import display_ml_page
from modules.ml.metricas import mostrar_metricas

def display():
    st.title('Modelo de Machine Learning')
    st.markdown("""
    Haz tu selección para saber si tu vuelo llegará con retraso o no con nuestro infalible modelo de predicción...
    """)

    display_ml_page()

    mostrar_metricas()
