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

    st.markdown("---")

    col1, col2 = st.columns([2, 5])
    with col1:
        st.write("Presentamos a continuación las métricas de rendimiento del modelo desarrollado utilizando DecisionTreeClassifier de scikit-learn. Estos indicadores te ayudarán a comprender la eficacia y precisión del modelo en la clasificación de datos.")
        st.image("sources/metricas.jpg")  # Mostrar imagen en la columna central
    with col2:
        mostrar_metricas()
