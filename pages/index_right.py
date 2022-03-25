# """
#     Import variable
# """
from dash import dcc, dash
from dash import html
from tabulate import tabulate

from style import external_stylesheets
from style import SIDEBAR_STYLE
from style import CONTENT_STYLE
import pandas as pd
from database_connect import df_merge
from style import *
from dash import html
import plotly.graph_objects as go
from dash import dash, dcc
from dash.dependencies import Input, Output
from plot import Selector
from database_connect import df_merge, df_specification
import plotly.express as px
from style import external_stylesheets
from plot import Private

"""
    Create HTML component
"""

#
# index_page = html.Div([
#     dcc.Link('Left', href='/left'),
#     html.Br(),
#     dcc.Link('Right', href='/right')
# ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

sliderbar = html.Div(
    [
        html.H2('Instrument'),
        html.Hr(),
        html.P(
            'Select device', className='lead',

        ),
        dcc.Link('Left:\nDY260722110', href='/left'),
        html.Br(),
        dcc.Link('Right:\nDY260662110', href='/right')
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id='page-content', style=CONTENT_STYLE)

app.layout = html.Div(children=[
    html.H1('Instrument:\nDY260662110', style={'marginLeft': '36rem',
                                               }),
    html.Div([
        dcc.Location(id='url'),
        sliderbar,
        content,

    ]),

    html.Div([
        dcc.Dropdown(
            ['High Mass', 'Low Mass'],
            id='mass-mode',
            placeholder='Mass mode'
        ),
        dcc.Dropdown(
            ['Positive', 'Negative'],
            id='polarity-dropdown',
            placeholder='Polarity'
        ),
        dcc.Dropdown(
            df_merge.scan_type.unique(),
            id='scan_type-dropdown',
            placeholder='Scan type'
        ),
        dcc.Dropdown(
            df_merge.scan_rate.unique(),
            id='scan_rate-dropdown',
            placeholder='Scan rate'
        ),
        dcc.Dropdown(

            ['Plotly, D3', 'G10',
             'T10', 'Alphabet', 'Dark24',
             'Light24', 'Set1', 'Pastel1',
             'Dark2', 'Set2', 'Pastel2',
             'Set3', 'Antique', 'Bold',
             'Pastel', 'Prism', 'Safe',
             'Vivid'

             ],
            id='line-color_1',
            placeholder='Line color'
        )

    ], style=RIGHT_COMPONENT_STYLE),

    html.Div([
        dcc.Graph(id='graph')
    ], style=GRAPH_STYLE),

    html.Div([
        dcc.Graph(id='graph_1_1'),
    ], style={'padding': '.100rem', 'marginTop': '4rem',
              'marginLeft': '205px', 'boxShadow': '#e3e3e3 4px 4px 2px',
              'border-radius': '10px', 'backgroundColor': 'white',
              'width': 1000, 'height': 455, 'left': 1000, 'top': 100}),

    html.Div([
        dcc.Graph(id='graph_2'),

    ], style=GRAPH_2_STYLE),

    html.Div([
        dcc.Graph(id='graph_3'),

    ], style=GRAPH_3_STYLE),

    html.Div([
        dcc.Dropdown(
            ['Plotly, D3', 'G10',
             'T10', 'Alphabet', 'Dark24',
             'Light24', 'Set1', 'Pastel1',
             'Dark2', 'Set2', 'Pastel2',
             'Set3', 'Antique', 'Bold',
             'Pastel', 'Prism', 'Safe',
             'Vivid'

             ],
            id='line-color_1_1',
            placeholder='Line color'
        ),

    ], style={'width': 150, 'marginTop': '-90rem', 'marginLeft': '18rem'}),

    html.Div([
        dcc.Dropdown(
            ['Plotly, D3', 'G10',
             'T10', 'Alphabet', 'Dark24',
             'Light24', 'Set1', 'Pastel1',
             'Dark2', 'Set2', 'Pastel2',
             'Set3', 'Antique', 'Bold',
             'Pastel', 'Prism', 'Safe',
             'Vivid'

             ],
            id='line-color_2',
            placeholder='Line color'
        )
    ], style={'width': 150, 'marginTop': '-50rem', 'marginLeft': '18rem'}),

    html.Div([
        dcc.Dropdown(
            ['Plotly, D3', 'G10',
             'T10', 'Alphabet', 'Dark24',
             'Light24', 'Set1', 'Pastel1',
             'Dark2', 'Set2', 'Pastel2',
             'Set3', 'Antique', 'Bold',
             'Pastel', 'Prism', 'Safe',
             'Vivid'

             ],
            id='line-color_3',
            placeholder='Line color'
        )
    ], style={'width': 150, 'marginTop': '90rem', 'marginLeft': '18rem'}),

], className='row')


def add_log(scale_value):
    if scale_value == 'Log':
        return True
    else:
        return False


def add_color(color):
    if color == 'Plotly':
        return px.colors.qualitative.Plotly

    elif color == 'D3':
        return px.colors.qualitative.D3

    elif color == 'G10':
        return px.colors.qualitative.G10

    elif color == 'T10':
        return px.colors.qualitative.T10

    elif color == 'Alphabet':
        return px.colors.qualitative.Alphabet

    elif color == 'Dark24':
        return px.colors.qualitative.Dark24

    elif color == 'Light24':
        return px.colors.qualitative.Light24

    elif color == 'Set1':
        return px.colors.qualitative.Set1

    elif color == 'Pastel1':
        return px.colors.qualitative.Pastel1

    elif color == 'Dark2':
        return px.colors.qualitative.Dark2

    elif color == 'Set2':
        return px.colors.qualitative.Set2

    elif color == 'Pastel2':
        return px.colors.qualitative.Pastel2

    elif color == 'Set3':
        return px.colors.qualitative.Set3

    elif color == 'Antique':
        return px.colors.qualitative.Antique

    elif color == 'Bold':
        return px.colors.qualitative.Bold

    elif color == 'Pastel':
        return px.colors.qualitative.Pastel

    elif color == 'Prism':
        return px.colors.qualitative.Prism

    elif color == 'Safe':
        return px.colors.qualitative.Safe

    elif color == 'Vivid':
        return px.colors.qualitative.Vivid


@app.callback(
    Output('graph', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value'),
    Input('line-color_1', 'value')
)
def update_graph(mass_mode, polarity, scan_type, scan_rate, color):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    fig = px.line(df_2, x='time', y='intensity', color='target_mass',
                  color_discrete_sequence=add_color(color))
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)

    return fig


@app.callback(
    Output('graph_1_1', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value'),
    Input('scale-button', 'value'),
    Input('line-color_1_1', 'value')
)
def update_graph_1_1(mass_mode, polarity, scan_type, scan_rate, scale_value, color):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    priv = Private(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    df_3 = priv.add_private()

    fig = px.line(df_3, x='time', y='mass_shift', color='target_mass',
                  color_discrete_sequence=add_color(color), log_y=add_log(scale_value))

    # fig.add_trace(
    #           go.Scatter(x = df_2['time'], y = df_spec['min_intensity'], marker=dict(
    #             color='red',showscale=False
    #         ), showlegend=False)
    #     )

    # fig = sel.add_treshold_2(fig)
    # fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    return fig


@app.callback(
    Output('graph_2', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value'),
    Input('line-color_2', 'value')

)
def update_fig_2(mass_mode, polarity, scan_type, scan_rate, color):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.create_df()
    fig = px.line(df_2, x='time', y='width', color='target_mass', color_discrete_sequence=add_color(color))
    fig.add_hline(0.6, line_dash="dash", line_color="red")
    fig.add_hline(0.8, line_dash="dash", line_color="red")
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    return fig


@app.callback(
    Output('graph_3', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value'),
    Input('line-color_3', 'value')

)
def update_fig_3(mass_mode, polarity, scan_type, scan_rate, color):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    fig = px.line(df_2, x='time', y='mass_shift', color='target_mass', color_discrete_sequence=add_color(color))
    fig.add_hline(y=0.1, line_dash="dash", line_color="red")
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    return fig


if __name__ == '__main__':
    app.run_server('0.0.0.0')


'DY260662110'