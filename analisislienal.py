import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def analisis_regresion_lineal_multiple():
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

    # Definir las variables independientes y dependientes
    X = df[['visitas']]
    y = df['seguidores']
    z = df['interacciones']

    # Crear y ajustar el modelo de regresión lineal para 'seguidores'
    model_y = LinearRegression()
    model_y.fit(X, y)
    y_pred = model_y.predict(X)
    intercept_y = model_y.intercept_
    coef_y = model_y.coef_[0]
    r2_y = r2_score(y, y_pred)

    # Crear y ajustar el modelo de regresión lineal para 'interacciones'
    model_z = LinearRegression()
    model_z.fit(X, z)
    z_pred = model_z.predict(X)
    intercept_z = model_z.intercept_
    coef_z = model_z.coef_[0]
    r2_z = r2_score(z, z_pred)

    # Crear una figura 3D con Plotly
    fig = go.Figure()

    # Añadir los puntos de datos reales
    fig.add_trace(go.Scatter3d(
        x=df['visitas'], 
        y=df['seguidores'], 
        z=df['interacciones'],
        mode='markers',
        marker=dict(size=5, color='blue', opacity=0.8),
        name='Datos Reales'
    ))

    # Añadir la superficie de regresión para 'seguidores'
    fig.add_trace(go.Scatter3d(
        x=df['visitas'], 
        y=y_pred, 
        z=df['interacciones'],
        mode='lines',
        line=dict(color='red', width=2),
        name=f'Regresión Seguidores<br>Intercepto: {intercept_y:.2f}<br>Coeficiente: {coef_y:.2f}<br>R²: {r2_y:.2f}'
    ))

    # Añadir la superficie de regresión para 'interacciones'
    fig.add_trace(go.Scatter3d(
        x=df['visitas'], 
        y=df['seguidores'], 
        z=z_pred,
        mode='lines',
        line=dict(color='green', width=2),
        name=f'Regresión Interacciones<br>Intercepto: {intercept_z:.2f}<br>Coeficiente: {coef_z:.2f}<br>R²: {r2_z:.2f}'
    ))

    # Configurar el layout del gráfico
    fig.update_layout(
        title='Regresión Lineal Múltiple: Visitas, Seguidores e Interacciones',
        scene=dict(
            xaxis_title='Visitas',
            yaxis_title='Seguidores',
            zaxis_title='Interacciones'
        )
    )

    return fig
