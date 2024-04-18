import streamlit as st
import pandas as pd
import plotly.express as px

def graficar_maxima_distancia_millas(df):
    # Crear una columna única que represente el par de aeropuertos en ambos sentidos
    df['par_aeropuertos'] = df.apply(lambda x: '-'.join(sorted([x['aeropuerto_origen'], x['aeropuerto_destino']])), axis=1)

    # Agrupar por este par y encontrar la distancia máxima entre ellos
    max_distancias = df.groupby('par_aeropuertos')['distancia_millas'].max().reset_index()

    # Ordenar por distancia de mayor a menor y tomar los top 20
    top_20_distancias = max_distancias.sort_values(by='distancia_millas', ascending=False).head(20)

    # Gráfico de barras con Plotly Express
    fig = px.bar(top_20_distancias, 
                 x='par_aeropuertos', 
                 y='distancia_millas', 
                 title='Top 20 Máxima Distancia en Millas entre Pares de Aeropuertos Únicos',
                 labels={'par_aeropuertos': 'Par de Aeropuertos', 'distancia_millas': 'Distancia en Millas'},
                 color='distancia_millas',
                 color_continuous_scale=px.colors.sequential.Viridis)

    fig.update_layout(
        title_x=0.5,
        xaxis={'categoryorder': 'total descending', 'title': 'Pares de Aeropuertos'},
        yaxis={'title': 'Máxima Distancia en Millas'},
        width=1080
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)