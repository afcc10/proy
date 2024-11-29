import pandas as pd
import plotly.graph_objects as go

def estadistica_descriptiva_seguidores():
    # Leer el archivo CSV
    df = pd.read_csv("../proy/csv/consolidado_data.csv")

    # Convertir la columna 'seguidores' a numérico si es necesario
    df["seguidores"] = pd.to_numeric(df["seguidores"], errors='coerce')

    # Convertir la columna 'Fecha' a datetime con inferencia automática del formato
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce', infer_datetime_format=True)

    # Verificar si hay valores NaT en la columna 'Fecha'
    if df["Fecha"].isna().sum() > 0:
        print("Advertencia: Algunos valores de fecha no se pudieron convertir.")

    # Obtener estadísticas específicas
    cantidad = df["seguidores"].count()
    media = df["seguidores"].mean()
    desviacion = df["seguidores"].std()
    valor_maximo = df["seguidores"].max()
    varianza = df["seguidores"].var()

    # Crear un DataFrame para las estadísticas
    estadisticas_df = pd.DataFrame({
        'Estadística': ['Cantidad de registros', 'Media', 'Desviación Estándar', 'Valor Máximo', 'Varianza'],
        'Valor': [cantidad, media, desviacion, valor_maximo, varianza]
    })

    # Formatear valores a dos decimales para las etiquetas
    estadisticas_df['Valor_Text'] = estadisticas_df['Valor'].apply(lambda x: f'{x:.2f}')

    # Agrupar por mes y calcular el promedio de visitas
    df['Mes'] = df['Fecha'].dt.to_period('M')
    df_mensual = df.groupby('Mes')['seguidores'].mean().reset_index()

    # Crear el gráfico de barras para las estadísticas generales
    fig1 = go.Figure(
        data=[
            go.Bar(
                x=estadisticas_df['Estadística'],
                y=estadisticas_df['Valor'],
                marker=dict(color=['skyblue', 'lightgreen', 'salmon', 'green', 'blue', 'red']),
                text=estadisticas_df['Valor_Text'],
                textposition='outside'
            )
        ],
        layout=go.Layout(
            title='Estadísticas de seguidores instagram',
            yaxis=dict(title='Valor'),
            xaxis=dict(title='Estadísticas')
        )
    )

    # Crear el gráfico de barras para el promedio de visitas por mes
    fig2 = go.Figure(
        data=[
            go.Bar(
                x=df_mensual['Mes'].astype(str),
                y=df_mensual['seguidores'],
                marker=dict(color=['skyblue', 'lightgreen', 'salmon', 'green', 'blue', 'orange', 'purple', 'yellow', 'red', 'brown', 'pink', 'grey']),
                text=[f'{v:.2f}' for v in df_mensual['seguidores']],
                textposition='outside'
            )
        ],
        layout=go.Layout(
            title='Promedio de seguidores por Mes',
            yaxis=dict(title='Promedio de Visitas'),
            xaxis=dict(title='Mes')
        )
    )

    return fig1, fig2
