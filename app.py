# app.py
import pandas as pd
import streamlit as st
from modules.config_page import set_global_page_config
from modules.create_sidebar import create_sidebar

set_global_page_config()

# Inicialización del estado de sesión para los DataFrames
def initialize_session_state():
    if 'df_dec_2021' not in st.session_state:
        st.session_state['df_dec_2021'] = pd.DataFrame()
    if 'df_dec_2022' not in st.session_state:
        st.session_state['df_dec_2022'] = pd.DataFrame()
    if 'df_dec_2023' not in st.session_state:
        st.session_state['df_dec_2023'] = pd.DataFrame()
    if 'df_todos' not in st.session_state:
        st.session_state['df_todos'] = pd.DataFrame()
    if 'df_modelo' not in st.session_state:
        st.session_state['df_modelo'] = pd.DataFrame()

initialize_session_state()

# Llama a la función de la barra lateral que crea el menú
create_sidebar()

