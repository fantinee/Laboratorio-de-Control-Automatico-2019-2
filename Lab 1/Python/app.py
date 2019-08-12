import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

from tank_system import TankSystem, TankSystemFake

tank_system = TankSystem()
tank_system.connect()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    # Title div
    html.Div([
        html.H1('Quadruple Tank Control'),
        html.Div(id='time_text')
    ]),

    html.Hr(),

    html.Div([
        # Graphs div
        html.Div([
            html.Div([
                html.Div(id='tank_3_text'),
                dcc.Graph(id='tank_3_graph'),
                html.Div(id='tank_1_text'),
                dcc.Graph(id='tank_1_graph'),
                html.Hr(),
                html.Div(id='valve_1_text'),
                dcc.Graph(id='valve_1_graph'),
                html.Div(id='tank_4_text'),
                dcc.Graph(id='tank_4_graph'),
                html.Div(id='tank_2_text'),
                dcc.Graph(id='tank_2_graph'),
                html.Hr(),
                html.Div(id='valve_2_text'),
                dcc.Graph(id='valve_2_graph')
            ], style={'columnCount': 2})
        ], className='nine columns'),

        # Settings div
        html.Div([
            # Status div
            html.Div([
                html.H3('Status'),
                html.Div(children='Disconnected'),
                html.Button(children='Connect'),
                html.Button(children='Disconnect')
                ]),

            html.Hr(),

            # Control mode div
            html.Div([
                html.H3('Control Mode'),
                dcc.RadioItems(
                    options=[
                        {'label': 'Manual', 'value': 'manual'},
                        {'label': 'Automatic', 'value': 'automatic'},
                    ],
                    value='manual'
                )
            ]),

            html.Hr(),

            # Manual mode div
            html.Div([
                html.H3('Manual Control'),
                html.Label('Valve 1'),
                dcc.Input(value=0, type='number'),
                html.Label('Valve 2'),
                dcc.Input(value=0, type='number')
            ]),

            html.Hr(),

            # Automatic mode div
            html.Div([
                html.H3('Automatic Control'),
                html.Label('Reference 1'),
                dcc.Input(value=0, type='number'),
                html.Label('Reference 2'),
                dcc.Input(value=0, type='number'),
                html.Label('Proportional gain'),
                dcc.Input(value=0, type='number'),
                html.Label('Integral gain'),
                dcc.Input(value=0, type='number'),
                html.Label('Derivative gain'),
                dcc.Input(value=0, type='number'),
                html.Label('Wind up limit'),
                dcc.Input(value=0, type='number'),
                html.Label('Derivative filter'),
                dcc.Input(value=0, type='number')
            ]),

            html.Hr(),

            # Logging div
            html.Div([
                html.H3('Logging'),
                html.Div(children='Status: not logging'),
                html.Button(children='Begin'),
                html.Button(children='Stop'),
                html.Label('Filename'),
                dcc.Input(value='log.csv', type='text')
            ]),
        ], className='three columns')
    ]),

    # 100 millisecond timer
    dcc.Interval(
        id='interval_component',
        interval= 1000,
        n_intervals=0
    )
])

@app.callback(Output('time_text', 'children'),
              [Input('interval_component', 'n_intervals')])
def update_metrics(n):
    return '{} seconds have passed.'.format(n)

@app.callback([Output('tank_1_text', 'children'),
               Output('tank_2_text', 'children'),
               Output('tank_3_text', 'children'),
               Output('tank_4_text', 'children'),
               Output('valve_1_text', 'children'),
               Output('valve_2_text', 'children')
               ],
              [Input('interval_component', 'n_intervals')])

def update_tanks_text(n):
    return ['Tank 1: {}'.format(tank_system.tank_1),
            'Tank 2: {}'.format(tank_system.tank_2),
            'Tank 3: {}'.format(tank_system.tank_3),
            'Tank 4: {}'.format(tank_system.tank_4),
            'Valve 1: {}'.format(tank_system.valve_1),
            'Valve 2: {}'.format(tank_system.valve_2),
            ]

# @app.callback([Output('tank_1_graph', 'figure'),
#                Output('tank_2_graph', 'figure'),
#                Output('tank_3_graph', 'figure'),
#                Output('tank_4_graph', 'figure'),
#                ],
#               [Input('interval_component', 'n_intervals')])
# def update_graphs(n):
#     return [{'data': [{'x': [1], 'y': [tank_system.tank_1], 'type': 'bar'}],
#             'layout': go.Layout(
#                 yaxis={'range': [0, 50]}
#             )},
#             {'data': [{'x': [1], 'y': [tank_system.tank_2], 'type': 'bar'}],
#              'layout': go.Layout(
#                  yaxis={'range': [0, 50]}
#              )},
#             {'data': [{'x': [1], 'y': [tank_system.tank_3], 'type': 'bar'}],
#              'layout': go.Layout(
#                  yaxis={'range': [0, 50]}
#              )},
#             {'data': [{'x': [1], 'y': [tank_system.tank_4], 'type': 'bar'}],
#              'layout': go.Layout(
#                  yaxis={'range': [0, 50]}
#              )}
#             ]

# @app.callback(Output('tank_4_graph', 'figure'),
#               [Input('interval_component', 'n_intervals')])
# def update_graphs(n):
#     return go.Figure(data=[1, 2, 3])


if __name__ == '__main__':
    app.run_server(debug=True)
