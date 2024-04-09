import streamlit as st
import plotly.express as px

def graficar_top_aerolineas_con_sin_retrasos(df):
    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    retrasos_aerolinea_llegada = retrasos_llegada.groupby(['aerolinea']).size().reset_index(name='con_retraso')
    sin_retraso_aerolinea = sin_retraso_llegada.groupby(['aerolinea']).size().reset_index(name='sin_retraso')

    retrasos_aerolinea = retrasos_aerolinea_llegada.merge(sin_retraso_aerolinea, on='aerolinea', how='left').fillna(0)

    # Crear un gráfico de barras
    fig = px.bar(retrasos_aerolinea, 
                 x='aerolinea', 
                 y=['con_retraso', 'sin_retraso'], 
                 title='Cantidad de vuelos con y sin retraso en la llegada por aerolínea',
                 labels={'aerolinea': 'Aerolínea', 'value': 'Cantidad de vuelos', 'variable': 'Estado del vuelo'},
                 opacity=0.7, 
                 color_discrete_map={"con_retraso": "red", "sin_retraso": "green"})

    fig.update_layout(title_x=0.5, xaxis={'categoryorder': 'total descending'})

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
