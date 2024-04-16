#paginas/modelo.py
# paginas/modelo.py
import streamlit as st
from modules.ml.prediccion import cargar_modelo

def display():
    st.title('Modelo de Machine Learning')
    st.markdown("""
    Haz tu selección para saber si tu vuelo llegará con retraso o no con nuestro infalible modelo de predicción...
    """)

    modelo_url = 'https://www.rubenmaestre.com/modelos/model.joblib'

    if st.button('Cargar modelo y predecir retraso'):
        modelo = cargar_modelo(modelo_url)
        st.write("Modelo cargado correctamente.")
        # Añadir más lógica para manejar la entrada del usuario y hacer predicciones aquí.
