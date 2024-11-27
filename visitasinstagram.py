import pandas as pd
import plotly.graph_objects as go

def generar_graficas():
    # Leer el archivo CSV
    df = pd.read_csv("C:/Users/USUARIO/Documents/proy/csv/visitas_instagram.csv")

    # Convertir la columna 'Primary' a numérico si es necesario
    df["Primary"] = pd.to_numeric(df["Primary"], errors='coerce')

    # Convertir la columna 'Fecha' a datetime
    df["Fecha"] = pd.to_datetime(df["Fecha"], format='%Y-%m-%d', errors='coerce')

    # Obtener estadísticas específicas
    cantidad = df["Primary"].count()
    media = df["Primary"].mean()
    desviacion = df["Primary"].std()
    valor_maximo = df["Primary"].max()
    varianza = df["Primary"].var()
   
    # Crear un DataFrame para las estadísticas
    estadisticas_df = pd.DataFrame({
        'Estadística': ['Cantidad de registros', 'Media', 'Desviación Estándar', 'Valor Máximo','Varianza'],
        'Valor': [cantidad, media, desviacion, valor_maximo,varianza]
    })

    # Agrupar por mes y calcular el promedio de visitas
    df['Mes'] = df['Fecha'].dt.to_period('M')
    df_mensual = df.groupby('Mes')['Primary'].mean().reset_index()

    # Crear el gráfico de barras para las estadísticas generales
    fig1 = go.Figure(
        data=[
            go.Bar(
                x=estadisticas_df['Estadística'],
                y=estadisticas_df['Valor'],
                marker=dict(color=['skyblue', 'lightgreen', 'salmon', 'green', 'blue','red']),
                text=estadisticas_df['Valor'],
                textposition='outside'
            )
        ],
        layout=go.Layout(
            title='Estadísticas de visitas instagram',
            yaxis=dict(title='Valor'),
            xaxis=dict(title='Estadísticas')
        )
    )

    # Crear el gráfico de barras para el promedio de visitas por mes
    fig2 = go.Figure(
        data=[
            go.Bar(
                x=df_mensual['Mes'].astype(str),
                y=df_mensual['Primary'],
                marker=dict(color=['skyblue', 'lightgreen', 'salmon', 'green', 'blue', 'orange', 'purple', 'yellow', 'red', 'brown', 'pink', 'grey']),
                text=df_mensual['Primary'],
                textposition='outside'
            )
        ],
        layout=go.Layout(
            title='Promedio de Visitas por Mes',
            yaxis=dict(title='Promedio de Visitas'),
            xaxis=dict(title='Mes')
        )
    )

    return fig1, fig2
