import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_estados_mas_retrasos(df):
    # Calculo de retrasos
    retrasos_llegada = df[df['retraso_llegada'] > 15]
    retrasos_estados_origen = retrasos_llegada.groupby(['estado_origen']).size().reset_index(name='con_retraso')

    # Filtrado para obtener los top 10 estados con más retrasos
    top_estados_mas_retrasos = retrasos_estados_origen.nlargest(10, 'con_retraso')

    # Gráfica
    fig = px.bar(top_estados_mas_retrasos, 
                 x='estado_origen', 
                 y='con_retraso', 
                 title='Top 10 Estados con más retrasos en la llegada',
                 labels={'estado_origen': 'Estado', 'con_retraso': 'Cantidad de retrasos'},
                 opacity=0.8, 
                 color_discrete_sequence=["red"])

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'})

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)

# Asumir que df ya está cargado o se carga en otra parte del código
# df = pd.read_csv('ruta_del_archivo.csv')
# graficar_estados_mas_retrasos(df)
