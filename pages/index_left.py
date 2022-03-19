# """
#     Import variable
# """
from dash import dcc, dash
from dash import html
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

], className='row')


@app.callback(
    Output('graph', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')
)
def update_graph(mass_mode, polarity, scan_type, scan_rate):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate,'DY260662110')
    df_2 = sel.select_target()
    fig = px.line(df_2, x='time', y='intensity', color='target_mass',
                  color_discrete_sequence=px.colors.sequential.Oryel, log_y = True)
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)



    return fig

@app.callback(
    Output('graph_1_1', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')
)
def update_graph_1_1(mass_mode, polarity, scan_type, scan_rate):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    sel_spec = Selector(df_specification, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_spec = sel_spec.create_df_spec()
    print(df_spec)
    fig = px.line(df_2, x='time', y='intensity', color='target_mass',
                    color_discrete_sequence=px.colors.sequential.Oranges, log_y = False)

    fig.add_trace(
          go.Scatter(x = df_2['time'], y = df_spec['min_intensity'], marker=dict(
            color='red',showscale=False
          ), showlegend=False)
    )
    fig = sel.add_treshold_2(fig)
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)

    return fig

@app.callback(
    Output('graph_2', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')

)
def update_fig_2(mass_mode, polarity, scan_type, scan_rate):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    fig = px.line(df_2, x='time', y='width', color='target_mass', color_discrete_sequence=px.colors.sequential.Oranges)
    fig.add_hline(0.6,line_dash="dash", line_color="red")
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
    Input('scan_rate-dropdown', 'value')

)
def update_fig_3(mass_mode, polarity, scan_type, scan_rate):
    sel = Selector(df_merge, mass_mode, polarity, scan_type, scan_rate, 'DY260662110')
    df_2 = sel.select_target()
    fig = px.line(df_2, x='time', y='mass_shift', color='target_mass', color_discrete_sequence=px.colors.sequential.Oranges)
    fig.add_hline(y=0.1,line_dash="dash", line_color="red")
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True)
    return fig

if __name__ == '__main__':
    app.run_server()