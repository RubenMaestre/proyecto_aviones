import streamlit as st
import plotly.express as px

def graficar_vuelos_por_aerolinea(df):
    # Asegúrate de que 'aerolinea' sea el nombre correcto de la columna en tu DataFrame
    vuelos_aerolinea = df.groupby(['aerolinea']).size().reset_index(name='Número total de vuelos')

    # Crear la figura con Plotly
    fig = px.bar(data_frame=vuelos_aerolinea,
                 x='aerolinea',
                 y='Número total de vuelos',
                 opacity=0.8,
                 title="Cantidad de vuelos nacionales por compañía aérea en Estados Unidos",
                 color='aerolinea')  # Asegúrate de que 'color' se refiera a una columna existente o elimínalo si no es necesario

    # Ajustar el tamaño de la gráfica y actualizar otros aspectos del layout
    fig.update_layout(
        title_x=0.5,
        xaxis_title='Compañías aéreas',
        yaxis_title='Cantidad total de vuelos',
        xaxis={'categoryorder': 'total descending'},
        width=1080,  # Ancho personalizado
        height=720   # Altura personalizada, ajusta según necesidad
    )
    
    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
