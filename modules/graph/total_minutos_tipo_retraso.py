import streamlit as st
import plotly.graph_objs as go

def graficar_total_minutos_por_tipo_retraso(df):
    tipos_retrasos = df[['tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion', 'tiempo_retraso_seguridad']]
    total_tipo = tipos_retrasos.sum()  # Suma total de los retrasos por tipo

    fig = go.Figure(data=[go.Bar(
        x=total_tipo.index,
        y=total_tipo.values,
        marker_color='skyblue'
    )])

    fig.update_layout(
        title='Total de minutos por cada tipo de retraso',
        xaxis_title='Tipo de retraso',
        yaxis_title='Total minutos',
        title_x=0.5,
        width=1080
    )

    # Mostrar la figura en la aplicación Streamlit
    st.plotly_chart(fig)
