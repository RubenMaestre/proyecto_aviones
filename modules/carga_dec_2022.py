import pandas as pd
import streamlit as st

def cargar_unir_2022():
    if 'df_dec_2022' not in st.session_state:
        archivo_1 = 'data/pickles/df_2022_1.pkl'
        archivo_2 = 'data/pickles/df_2022_2.pkl'

        df_2022_1 = pd.read_pickle(archivo_1)
        df_2022_2 = pd.read_pickle(archivo_2)

        st.session_state.df_dec_2022 = pd.concat([df_2022_1, df_2022_2], ignore_index=True)

    df_dec_2022 = st.session_state.df_dec_2022
    return df_dec_2022
