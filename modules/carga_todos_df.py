from .carga_dec_2021 import cargar_unir_2021  # Asegúrate de que el nombre de la función sea correcto
from .carga_dec_2022 import cargar_unir_2022
from .carga_dec_2023 import cargar_unir_2023
import pandas as pd

def cargar_todos_df():
    # Cargar cada DataFrame de año
    df_dec_2021 = cargar_unir_2021()
    df_dec_2022 = cargar_unir_2022()
    df_dec_2023 = cargar_unir_2023()

    # Unir todos los DataFrames en uno solo
    df_todos = pd.concat([df_dec_2021, df_dec_2022, df_dec_2023], ignore_index=True)

    return df_todos
