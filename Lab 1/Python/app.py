import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import threading
import pandas
from dash.exceptions import PreventUpdate
import time

from tank_system import TankSystem
from controller import Controller


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
                dcc.RadioItems(
                    id='status_items',
                    options=[
                        {'label': 'Connected', 'value': 'connected'},
                        {'label': 'Disconnected', 'value': 'disconnected'},
                    ],
                    value='disconnected'
                )
            ]),

            html.Hr(),

            # Control mode div
            html.Div([
                html.H3('Control Mode'),
                dcc.RadioItems(
                    id='control_mode_items',
                    options=[
                        {'label': 'Automatic', 'value': 'automatic'},
                        {'label': 'Manual', 'value': 'manual'},
                    ],
                    value='manual'
                )
            ]),

            html.Hr(),

            # Manual mode div
            html.Div([
                html.H3('Manual Control'),
                html.Div([
                    html.Label('Valve 1'),
                    dcc.Input(id='valve_1_input', value=0, type='number', min=-1,
                              max=1, step='any', style={'width': 150}),
                    html.Label('Valve 2'),
                    dcc.Input(id='valve_2_input', value=0, type='number', min=-1,
                              max=1, step='any', style={'width': 150})
                    ], style={'columnCount': 2})
            ]),

            html.Hr(),

            # Automatic mode div
            html.Div([
                html.H3('Automatic Control'),
                html.Div([
                    html.Label('Reference 1'),
                    dcc.Input(id='ref_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Proportional gain 1'),
                    dcc.Input(id='kp_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Integral gain 1'),
                    dcc.Input(id='ki_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Derivative gain 1'),
                    dcc.Input(id='kd_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Wind up limit 1'),
                    dcc.Input(id='windup_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Derivative filter 1'),
                    dcc.Input(id='d_filter_1_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Reference 2'),
                    dcc.Input(id='ref_2_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Proportional gain 2'),
                    dcc.Input(id='kp_2_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Integral gain 2'),
                    dcc.Input(id='ki_2_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Derivative gain 2'),
                    dcc.Input(id='kd_2_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Wind up limit 2'),
                    dcc.Input(id='windup_2_input', value=0, type='number',
                              min=0, style={'width': 150}),
                    html.Label('Derivative filter 2'),
                    dcc.Input(id='d_filter_2_input', value=0, type='number',
                              min=0, style={'width': 150})
                    ], style={'columnCount': 2})
            ]),

            html.Hr(),

            # Logging div
            html.Div([
                html.H3('Logging'),
                dcc.RadioItems(
                    id='logging_items',
                    options=[
                        {'label': 'On', 'value': 'on'},
                        {'label': 'Off', 'value': 'off'},
                    ],
                    value='off'
                ),
                html.Label('Filename'),
                dcc.Input(value='log.csv', type='text')
            ]),
        ], className='three columns')
    ]),

    # Graph timer
    dcc.Interval(
        id='graph_interval',
        interval= 1000,
        n_intervals=0
    ),

    html.Div(id='hidden_div', style={'display': 'none'})
])


@app.callback(Output('time_text', 'children'),
              [Input('graph_interval', 'n_intervals')])
def update_test_text(n):
    #print(tank_system.sub_handler.tanks_alarms)
    return '{} seconds have passed.'.format(n)


@app.callback([Output('tank_1_text', 'children'),
               Output('tank_2_text', 'children'),
               Output('tank_3_text', 'children'),
               Output('tank_4_text', 'children'),
               Output('valve_1_text', 'children'),
               Output('valve_2_text', 'children')
               ],
              [Input('graph_interval', 'n_intervals')])
def update_tanks_text(n):
    if tank_system.connected and all(tank_system.past_values.values()):
        return ['Tank 1: {:.2f}{}'.format(
                    tank_system.past_values['tank_1'][-1],
                    ' (ALARM)' if tank_system.sub_handler.tanks_alarms[1]
                    else ''),
                'Tank 2: {:.2f}{}'.format(
                    tank_system.past_values['tank_2'][-1],
                    ' (ALARM)' if tank_system.sub_handler.tanks_alarms[2]
                    else ''),
                'Tank 3: {:.2f}{}'.format(
                    tank_system.past_values['tank_3'][-1],
                    ' (ALARM)' if tank_system.sub_handler.tanks_alarms[3]
                    else ''),
                'Tank 4: {:.2f}{}'.format(
                    tank_system.past_values['tank_4'][-1],
                    ' (ALARM)' if tank_system.sub_handler.tanks_alarms[4]
                    else ''),
                'Valve 1: {:.2f}'.format(
                    tank_system.past_values['valve_1'][-1]),
                'Valve 2: {:.2f}'.format(
                    tank_system.past_values['valve_2'][-1]),
                ]
    else:
        return ['Tank 1: Not connected',
                'Tank 2: Not connected',
                'Tank 3: Not connected',
                'Tank 4: Not connected',
                'Valve 1: Not connected',
                'Valve 2: Not connected']


@app.callback([Output('tank_1_graph', 'figure'),
               Output('tank_2_graph', 'figure'),
               Output('tank_3_graph', 'figure'),
               Output('tank_4_graph', 'figure'),
               Output('valve_1_graph', 'figure'),
               Output('valve_2_graph', 'figure'),
               ],
              [Input('graph_interval', 'n_intervals')])
def update_graphs(n):
    return [{'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['tank_1'])}],
            'layout': go.Layout(
                yaxis={'range': [0, 50]}
            )},
            {'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['tank_2'])}],
             'layout': go.Layout(
                 yaxis={'range': [0, 50]}
             )},
            {'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['tank_3'])}],
             'layout': go.Layout(
                 yaxis={'range': [0, 50]}
             )},
            {'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['tank_4'])}],
             'layout': go.Layout(
                 yaxis={'range': [0, 50]}
             )},
            {'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['valve_1'])}],
             'layout': go.Layout(
                 yaxis={'range': [-1, 1]}
             )},
            {'data': [{'x': list(tank_system.past_values['time']),
                       'y': list(tank_system.past_values['valve_2'])}],
             'layout': go.Layout(
                 yaxis={'range': [-1, 1]}
             )}
            ]


@app.callback(Output('status_items', 'style'),
              [Input('status_items', 'value')])
def status_items(value):
    if value == 'disconnected':
        print('System disconnected')
        tank_system.disconnect()
    elif value == 'connected':
        print('System connected')
        tank_system.connect()
    raise PreventUpdate


@app.callback(Output('control_mode_items', 'style'),
              [Input('control_mode_items', 'value')])
def control_mode_items(value):
    if value == 'manual':
        print('Manual mode activated')
        controllers[0].active = False
        controllers[1].active = False
    elif value == 'automatic':
        print('Automatic mode activated')
        controllers[0].active = True
        controllers[1].active = True
    raise PreventUpdate


@app.callback(Output('valve_1_input', 'style'),
              [Input('valve_1_input', 'value')])
def valve_1_input(value):
    if not controllers[0].active and tank_system.connected and value is not \
            None:
        print('Valve 1 set to {}'.format(value))
        tank_system.valve_1 = value
    raise PreventUpdate


@app.callback(Output('valve_2_input', 'style'),
              [Input('valve_2_input', 'value')])
def valve_2_input(value):
    if not controllers[1].active and tank_system.connected and value is not \
            None:
        print('Valve 2 set to {}'.format(value))
        tank_system.valve_2 = value
    raise PreventUpdate


@app.callback(Output('ref_1_input', 'style'),
              [Input('ref_1_input', 'value')])
def ref_1_input(value):
    if value is not None:
        print('Reference 1 set to {}'.format(value))
        controllers[0].ref = value
    raise PreventUpdate


@app.callback(Output('kp_1_input', 'style'),
              [Input('kp_1_input', 'value')])
def kp_1_input(value):
    if value is not None:
        print('Proportional constant 1 set to {}'.format(value))
        controllers[0].k_p = value
    raise PreventUpdate


@app.callback(Output('ki_1_input', 'style'),
              [Input('ki_1_input', 'value')])
def ki_1_input(value):
    if value is not None:
        print('Integral constant 1 set to {}'.format(value))
        controllers[0].k_i = value
    raise PreventUpdate


@app.callback(Output('kd_1_input', 'style'),
              [Input('kd_1_input', 'value')])
def kd_1_input(value):
    if value is not None:
        print('Derivative constant 1 set to {}'.format(value))
        controllers[0].k_d = value
    raise PreventUpdate


@app.callback(Output('windup_1_input', 'style'),
              [Input('windup_1_input', 'value')])
def windup_1_input(value):
    if value is not None:
        print('Windup limit 1 set to {}'.format(value))
        controllers[0].windup = value
    raise PreventUpdate


@app.callback(Output('d_filter_1_input', 'style'),
              [Input('d_filter_1_input', 'value')])
def d_filter_1_input(value):
    if value is not None:
        print('Derivative filter 1 set to {}'.format(value))
        controllers[0].d_filter = value
    raise PreventUpdate


@app.callback(Output('ref_2_input', 'style'),
              [Input('ref_2_input', 'value')])
def ref_2_input(value):
    if value is not None:
        print('Reference 2 set to {}'.format(value))
        controllers[1].ref = value
    raise PreventUpdate


@app.callback(Output('kp_2_input', 'style'),
              [Input('kp_2_input', 'value')])
def kp_2_input(value):
    if value is not None:
        print('Proportional constant 2 set to {}'.format(value))
        controllers[1].k_p = value
    raise PreventUpdate


@app.callback(Output('ki_2_input', 'style'),
              [Input('ki_2_input', 'value')])
def ki_2_input(value):
    if value is not None:
        print('Integral constant 2 set to {}'.format(value))
        controllers[1].k_i = value
    raise PreventUpdate


@app.callback(Output('kd_2_input', 'style'),
              [Input('kd_2_input', 'value')])
def kd_2_input(value):
    if value is not None:
        print('Derivative constant 2 set to {}'.format(value))
        controllers[1].k_d = value
    raise PreventUpdate


@app.callback(Output('windup_2_input', 'style'),
              [Input('windup_2_input', 'value')])
def windup_2_input(value):
    if value is not None:
        print('Windup limit 2 set to {}'.format(value))
        controllers[1].windup = value
    raise PreventUpdate


@app.callback(Output('d_filter_2_input', 'style'),
              [Input('d_filter_2_input', 'value')])
def d_filter_2_input(value):
    if value is not None:
        print('Derivative filter 2 set to {}'.format(value))
        controllers[1].d_filter = value
    raise PreventUpdate


def logger():
    global last_time
    threading.Timer(0.1, logger).start()

    tank_system.log_values()

    if (tank_system.connected and controllers[0].active
        and controllers[1].active):
        time_dif = time.time() - last_time
        last_time = time.time()
        tank_system.valve_1 = controllers[0].pid_control(
            tank_system.past_values['tank_1'][-1], time_dif)
        tank_system.valve_2 = controllers[1].pid_control(
            tank_system.past_values['tank_2'][-1], time_dif)


def alarm_resetter():
    threading.Timer(5, alarm_resetter).start()
    tank_system.sub_handler.tanks_alarms = {1: False, 2: False, 3: False,
                                            4: False}

if __name__ == '__main__':
    tank_system = TankSystem()
    controllers = [Controller(1), Controller(2)]
    last_time = time.time()


    logger()
    alarm_resetter()

    app.run_server(debug=True)
