# modules/ml/prediccion.py
import pandas as pd
import streamlit as st
import joblib
import requests
from io import BytesIO

def cargar_modelo(url):
    response = requests.get(url)
    modelo = joblib.load(BytesIO(response.content))
    return modelo


