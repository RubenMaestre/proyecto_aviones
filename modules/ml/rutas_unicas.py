from modules.carga_todos_df import cargar_todos_df

def obtener_rutas_unicas():
    df_todos = cargar_todos_df()
    # Seleccionar las columnas de interés y eliminar duplicados para obtener rutas únicas
    rutas_unicas = df_todos[['ciudad_origen', 'ciudad_destino']].drop_duplicates()
    return rutas_unicas
