import dash
from dash import dcc, html
from visitasinstagram import generar_graficas  # Importa la función desde tu archivo de funciones
from publicoinstagram import grafico_rango_edad_genero  # Importa la función
from principales_paises import grafico_paises_instagram  # Importa la nueva función
from principales_ciudades import grafico_ciudades_instagram
from consolidado import graficos_consolidados_separados # Importa la nueva función
from dispersionInteraccionesAlcance import grafico_dispersion # Importa la nueva función
from analisislienal import analisis_regresion_lineal_multiple # Importa la nueva función
from alcanceinstagram import estadistica_descriptiva_alcance # Importa la nueva función
from seguidoresinstagram import estadistica_descriptiva_seguidores
from analisiscorrelacion import analisis_correlacion # Importa la nueva función
from analisislinealvisitas import regresion_lineal_visitas_seguidores

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Obtener las figuras desde las funciones
fig1, fig2 = generar_graficas()
fig3 = grafico_rango_edad_genero()
fig4 = grafico_paises_instagram()
fig5 = grafico_ciudades_instagram()
figuras_consolidadas = graficos_consolidados_separados()
fig_dispersion = grafico_dispersion()
fig_analisis_lineal = analisis_regresion_lineal_multiple() 
fig_alcance1, fig_alcance2 = estadistica_descriptiva_alcance()
fig_seguidores1, fig_seguidores2 = estadistica_descriptiva_seguidores()
fig_correlacion = analisis_correlacion()
fig_regresion = regresion_lineal_visitas_seguidores()

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Estadisticas en Instagram"),
    
    dcc.Tabs([
        dcc.Tab(label='Estadísticas Generales', children=[
            dcc.Graph(id='estadisticas-generales', figure=fig1),
            dcc.Graph(id='alcance-estadisticas', figure=fig_alcance1),
            dcc.Graph(id='alcance-seguidores', figure=fig_seguidores1)
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Promedios por Mes', children=[
            dcc.Graph(id='promedio-visitas-mes', figure=fig2),
            dcc.Graph(id='alcance-promedio-mes', figure=fig_alcance2),
            dcc.Graph(id='seguidores-promedio-mes', figure=fig_seguidores2)
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Distribución por Rango de Edad y Género', children=[
            dcc.Graph(id='grafico-rango-edad-genero', figure=fig3)
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Distribución por País', children=[
            dcc.Graph(id='grafico-paises-instagram', figure=fig4)
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Distribución por Ciudad', children=[
            dcc.Graph(id='grafico-ciudades-instagram', figure=fig5)
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        # Añadir una pestaña para los gráficos consolidados separados
        dcc.Tab(label='Suma Mensual de Métricas Consolidadas', children=[
            *[
                dcc.Graph(id=f'graficos-consolidados-separados-{columna}', figure=fig)
                for columna, fig in figuras_consolidadas.items()
            ]
        ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Gráfico de Dispersión', children=[ 
                dcc.Graph(id='grafico-dispersion', figure=fig_dispersion) 
                ], style={'font-family': 'Arial', 'font-size': '16px'}),
        dcc.Tab(label='Análisis Lineal', children=[ 
                dcc.Graph(id='analisis-correlacion', figure=fig_correlacion),
                dcc.Graph(id='regresion-lineal', figure=fig_analisis_lineal),
                dcc.Graph(id='regresion-lineal_vis_seg', figure=fig_regresion)
                #dcc.Graph(id='regresion-lineal-seguidores',figure=fig_regresion2)
                ], 
                style={'font-family': 'Arial', 'font-size': '16px'})
    ])
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
