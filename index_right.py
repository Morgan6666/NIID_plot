"""
    Import variable
"""
from dash import dcc, dash
from dash import html
from style import external_stylesheets
from style import SIDEBAR_STYLE
from style import CONTENT_STYLE
import pandas as pd
from database_connect import df_merge
from style import *

"""
    Create HTML component
"""
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# index_page = html.Div([
#     dcc.Link('Left', href='/left'),
#     html.Br(),
#     dcc.Link('Right', href='/right')
# ])

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

    ], style=RIGHT_COMPONENT_STYLE),

    html.Div([
        dcc.Graph(id='graph',
                  )
    ], style=GRAPH_STYLE),

    html.Div([
        dcc.Graph(id='graph_1_1')
    ], style=GRAPH_1_1_STYLE),

    html.Div([
        dcc.Graph(id='graph_2')

    ], style=GRAPH_2_STYLE),

    html.Div([
        dcc.Graph(id='graph_3')
    ], style=GRAPH_3_STYLE)

])
