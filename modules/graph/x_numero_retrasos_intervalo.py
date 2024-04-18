import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_retrasos_por_intervalo(df):
    # Crear intervalos de 5 minutos hasta el máximo retraso más un pequeño buffer
    intervalos = list(range(0, df['retraso_llegada'].max() + 6, 5))
    df['intervalo'] = pd.cut(df['retraso_llegada'], bins=intervalos, right=False)  # Categorizar los retrasos en estos intervalos

    # Agrupar por intervalo y contar ocurrencias
    tabla = df.groupby('intervalo').size().reset_index(name='numero_de_retrasos')
    tabla['intervalo'] = tabla['intervalo'].astype(str)  # Convertir el intervalo a string para visualización

    # Filtrar intervalos con al menos un retraso y excluir el primer intervalo (generalmente 0)
    tabla_filtrada = tabla[tabla['numero_de_retrasos'] >= 1][1:]  # Excluye el primer rango si es necesario

    # Calcular la mediana de los números de retrasos
    mediana_retrasos = tabla_filtrada['numero_de_retrasos'].median()

    # Crear el gráfico de barras
    fig = px.bar(tabla_filtrada[:40],  # Limitar a los primeros 40 intervalos para mejor visualización
                 x='intervalo', 
                 y='numero_de_retrasos', 
                 opacity=0.8,
                 title='Número de Retrasos por Intervalo (Hasta 200 Minutos)',
                 labels={'intervalo': 'Intervalo de Retraso', 'numero_de_retrasos': 'Número de Retrasos'})

    # Configurar el layout del gráfico
    fig.update_layout(
        title_x=0.5,  # Centrar el título
        xaxis_title='Intervalo de Retraso',
        yaxis_title='Número de Retrasos'
    )

    # Agregar una línea vertical para la mediana
    fig.add_vline(x=mediana_retrasos, line_dash="dash", line_color="green", annotation_text="Mediana", annotation_position="top left")

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)