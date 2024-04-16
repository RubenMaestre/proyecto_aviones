#paginas/modelo.py
import streamlit as st
from modules.ml.prediccion import cargar_modelo, hacer_prediccion, cargar_datos

def display():
    st.title('Modelo de Machine Learning')
    st.markdown("""
    Haz tu selección para saber si tu vuelo llegará con retraso o no con nuestro infalible modelo de predicción...
    """)

    # Cargar el modelo y los datos
    modelo = cargar_modelo('data/joblib/model.joblib')
    datos = cargar_datos('data/df_modelo.parquet')

    # Añade aquí código para capturar la entrada del usuario y realizar predicciones
    # Por ejemplo, podrías tener un formulario para que los usuarios ingresen los detalles del vuelo

    if st.button('Predice el retraso'):
        resultado = hacer_prediccion(modelo, datos)  # Asegúrate de ajustar esta llamada a las necesidades reales
        st.write(f"Resultado de la predicción: {resultado}")