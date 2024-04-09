import pandas as pd

def cargar_unir_2023():
    # Rutas a los archivos pickle
    archivo_1 = 'data/pickles/df_2023_1.pkl'
    archivo_2 = 'data/pickles/df_2023_2.pkl'

    # Cargar los DataFrames desde los archivos pickle
    df_2023_1 = pd.read_pickle(archivo_1)
    df_2023_2 = pd.read_pickle(archivo_2)

    # Unir los dos DataFrames en uno solo
    df_dec_2023 = pd.concat([df_2023_1, df_2023_2], ignore_index=True)

    return df_dec_2023
