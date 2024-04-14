import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def cargar_unir_2023():
    if 'df_dec_2023' not in st.session_state:
        archivo_1 = 'data/pickles/df_2023_1.pkl'
        archivo_2 = 'data/pickles/df_2023_2.pkl'

        df_2023_1 = pd.read_pickle(archivo_1)
        df_2023_2 = pd.read_pickle(archivo_2)

        st.session_state.df_dec_2023 = pd.concat([df_2023_1, df_2023_2], ignore_index=True)

    df_dec_2023 = st.session_state.df_dec_2023
    return df_dec_2023
