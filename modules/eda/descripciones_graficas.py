# modules/eda/descripciones_graficas.py
import pandas as pd

def cargar_descripciones():
    """Carga las descripciones de las gráficas desde un archivo Excel y verifica las columnas."""
    try:
        # Asegúrate de especificar la ruta completa si el archivo no está en el mismo directorio que este script.
        df_descripciones = pd.read_excel('data/graficas/comentarios.xlsx')
        # Verifica que las columnas esperadas existan en el DataFrame
        if 'Año' not in df_descripciones.columns or 'Nombre' not in df_descripciones.columns:
            print("Las columnas 'Año' o 'Nombre' no están presentes en el DataFrame.")
            print("Columnas encontradas:", df_descripciones.columns)
            return pd.DataFrame()
        return df_descripciones
    except Exception as e:
        print(f"Error al cargar las descripciones: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío si hay error

def obtener_descripcion(año, nombre_grafica, df_descripciones):
    """Busca y retorna la descripción para una gráfica específica dada por año y nombre."""
    try:
        descripcion = df_descripciones[
            (df_descripciones['Año'] == año) & (df_descripciones['Nombre'] == nombre_grafica)
        ]['Descripción'].values

        if descripcion.size > 0:
            return descripcion[0]
        else:
            return "Descripción no disponible."
    except Exception as e:
        print(f"Error al obtener la descripción: {e}")
        return "Descripción no disponible."