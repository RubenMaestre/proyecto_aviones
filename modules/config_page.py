# modules/config_page.py
import streamlit as st

def set_global_page_config():
    st.set_page_config(
        page_title="Análisis de Puntualidad en Aeropuertos",
        page_icon="✈️",
        layout="wide"
    )
