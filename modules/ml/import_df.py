import pandas as pd
import streamlit as st


def cargar_df_modelo():
    return pd.read_parquet('data/df_modelo.parquet')