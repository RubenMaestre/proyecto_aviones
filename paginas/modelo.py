#paginas/modelo.py
import streamlit as st
import streamlit as st
from modules.ml.prediccion import cargar_modelo, hacer_prediccion

def display():
    st.title('Modelo de Machine Learning')
    st.markdown("""
    Haz tu selección para saber si tu vuelo llegará con retraso o no con nuestro infalible modelo de predicción...
    """)

    # Botón para cargar el modelo y hacer una predicción
    if st.button('Cargar modelo y predecir retraso'):
        # Cargar el modelo solo cuando el usuario lo solicite
        modelo = cargar_modelo('data/joblib/model.joblib')
        st.write("Modelo cargado correctamente.")