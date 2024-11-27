import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def grafico_reales_vs_predichas():
    # Leer el archivo CSV
    df = pd.read_csv('C:/Users/USUARIO/Documents/proy/csv/consolidado_data.csv')

    # Preparar los datos
    X = df[['alcance']]
    y = df['visitas']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear y ajustar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = model.predict(X_test)

    # Gráfico: Visitas Reales vs Predichas
    fig1 = px.scatter(x=y_test, y=y_pred, title='Visitas Reales vs Predichas', labels={'x': 'Visitas Reales', 'y': 'Visitas Predichas'})
    fig1.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], mode='lines', line=dict(color='red', dash='dash'), name='Línea de Referencia'))

    # Gráfico: Distribución de Residuos
    residuals = y_test - y_pred
    fig2 = px.histogram(residuals, nbins=30, title='Distribución de Residuos', labels={'value': 'Residuos (Errores)', 'count': 'Frecuencia'})
    fig2.add_trace(go.Scatter(x=[0, 0], y=[0, residuals.count()], mode='lines', line=dict(color='red', dash='dash'), name='Línea de Referencia'))

    return fig1, fig2
