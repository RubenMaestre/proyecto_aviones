# modules/ml/prediccion.py
import pandas as pd
import streamlit as st
import joblib

# Función para cargar el modelo
def cargar_modelo(path):
    return joblib.load(path)

# Función para realizar una predicción
def hacer_prediccion(modelo, datos):
    return modelo.predict(datos)

# Función para cargar datos
def cargar_datos(path):
    return pd.read_parquet(path)
