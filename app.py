# app.py
from modules.config_page import set_global_page_config
set_global_page_config()

import streamlit as st
from modules.create_sidebar import create_sidebar

# Llama a la función de la barra lateral que crea el menú
create_sidebar()
