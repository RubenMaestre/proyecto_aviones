# modules/ml/prediccion.py
import pandas as pd
import streamlit as st
import joblib

def cargar_modelo(path):
    # Esta función carga el modelo desde un archivo joblib
    modelo = joblib.load(path)
    return modelo

# Función para realizar una predicción
def hacer_prediccion(modelo, datos):
    return modelo.predict(datos)

