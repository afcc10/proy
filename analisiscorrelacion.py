import pandas as pd
import plotly.graph_objects as go

def analisis_correlacion():
    # Leer el archivo CSV
    df = pd.read_csv("C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv")

    # Convertir la columna 'Fecha' a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

    # Asegurarse de que las columnas relevantes sean numéricas
    df["alcance"] = pd.to_numeric(df["alcance"], errors='coerce')
    df["seguidores"] = pd.to_numeric(df["seguidores"], errors='coerce')
    df["visitas"] = pd.to_numeric(df["visitas"], errors='coerce')
    df["contactos_mensajes"] = pd.to_numeric(df["contactos_mensajes"], errors='coerce')
    df["clic_en_enlace"] = pd.to_numeric(df["clic_en_enlace"], errors='coerce')
    df["interacciones"] = pd.to_numeric(df["interacciones"], errors='coerce')

    # Crear la matriz de correlación
    corr = df[['contactos_mensajes', 'seguidores', 'alcance', 'clic_en_enlace', 'interacciones', 'visitas']].corr()

    # Crear el heatmap de correlación con Plotly
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale='Viridis',  # Usar una paleta de colores predefinida
        zmin=-1, zmax=1,
        text=corr.values,
        texttemplate='%{text:.2f}'
    ))
    fig.update_layout(
        title='Matriz de Correlación',
        xaxis_title='Variables',
        yaxis_title='Variables'
    )

    return fig
