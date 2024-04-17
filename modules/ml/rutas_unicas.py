from modules.carga_todos_df import cargar_todos_df

def obtener_rutas_unicas():
    df_todos = cargar_todos_df()
    # Asegúrate de que el dataframe incluya las columnas 'estado_origen', 'ciudad_origen', 'estado_destino' y 'ciudad_destino'
    rutas_unicas = df_todos[['estado_origen', 'ciudad_origen', 'estado_destino', 'ciudad_destino']].drop_duplicates()
    return rutas_unicas

