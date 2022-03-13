import os
import plotly.io as pio
import plotly
import plotly.express as px
import dash
from dash import dcc
from dash import html
import datetime
import sd_material_ui
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State, ClientsideFunction
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
from dash import dcc
from database_connect import Connection
from sqlalchemy import create_engine
import asyncio
import psycopg2
from tabulate import tabulate
import numpy as np

WIDTH_0 = 0.6
WIDTH_1 = 0.8
pio.templates.default = 'plotly_white'
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()
conect = Connection(engine, 'tests.txt', 'standards.txt', 'results.txt')
# df_result = conect.create_df_result()
df_merge = conect.create_merge()
df_merge = df_merge.drop('id', axis=1)

target_mass = df_merge.target_mass.unique()


def create_df(df, mass_mode, polarity, scan_type, scan_rate,instrument, mass = None,):
    df = df[(df['instrument'] == instrument)
            &  (df['scan_type'] == scan_type)
            & (df['mass_mode'] == mass_mode)
            & (df['polarity'] == polarity)
            & (df['scan_rate'] == scan_rate)].sort_values(by = ['time']).round({'target_mass': 0})

    df['target_mass'] = df['target_mass'].replace('', np.nan).astype('Int64')



    return df


def select_q1_high_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_type == 'Q1 MS' and mass_mode == 'High Mass' and polarity == 'Positive' and scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q1_high_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q1_low_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q1_low_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q3_low_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_type == 'Q1 MS' and mass_mode == 'Low Mass' and polarity == 'Negative' and scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q3_low_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q3_high_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_q3_high_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if scan_rate == 10:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 200:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 1000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 2000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif scan_rate == 20000:
        df = create_df(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def select_target(df, mass_mode, polarity, scan_type, scan_rate, instrument):
    if mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':
        df = select_q1_high_positive(df_merge, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df
    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        df = select_q1_high_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df
    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':
        df = select_q1_low_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df
    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        df = select_q1_low_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df
    elif mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        df = select_q3_high_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        df = select_q3_high_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        df = select_q3_low_positive(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df

    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        df = select_q3_low_negative(df, mass_mode, polarity, scan_type, scan_rate, instrument)
        return df


def add_tresh_h_q1(polarity, scan_type, scan_rate, mass):

    if polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
        if mass == 500.380:
            y_0 = 3.2e7
            return y_0
        elif mass == 616.464:
            y_0 = 2.0e7
            return y_0

        elif mass == 906.673:
            y_0 = 9.6e7
            return y_0

        elif mass == 1952.427:
            y_0 = 2.4e6
            return y_0

    elif polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
        if mass == 933.636:
            y_0 = 1.8e7
            return y_0

        elif mass == 1863.306:
            y_0 = 1.0e6
            return y_0


def add_tresh_l_q1(polarity, scan_type, scan_rate, mass):

    if polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
        if mass == 175.133:
            y_0 = 8.0e6
            return y_0

        elif mass == 500.380:
            y_0 = 3.68e7
            return y_0

        elif mass == 616.464:
            y_0 = 2.4e7
            return y_0

        elif mass ==  906.673:
            y_0 = 1.0e8
            return y_0

    if polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
        if mass == 933.636:
            y_0 = 1.8e7
            return y_0

def add_tresh_h_q3(polarity, scan_type, scan_rate, mass):
    if polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        if mass == 500.380:
            y_0 = 3.2e7
            return y_0

        elif mass == 616.463:
            y_0 = 2.0e7
            return y_0

        elif mass == 906.673:
            y_0 = 9.6e7
            return y_0

        elif mass == 1952.427:
            y_0 = 2.4e6
            return y_0

    elif polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        if mass == 933.636:
            y_0 = 1.8e7
            return y_0

        elif mass == 1863.306:
            y_0 = 1.0e6
            return y_0


def add_tresh_l_q3(polarity, scan_type, scan_rate, mass):
    if polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        if mass == 175.133:
            y_0  = 8.0e6
            return y_0

        elif mass == 500.380:
            y_0 = 3.68e7
            return y_0

        elif mass == 616.464:
            y_0 = 2.4e7
            return y_0

        elif mass == 906.673:
            y_0 = 1.0e8
            return y_0

    elif polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        if mass == 933.636:
            y_0 = 1.8e7
            return y_0




def add_treshold(mass_mode, polarity, scan_type, scan_rate, mass):

    if mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
       add_tresh_h_q1(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
       add_tresh_h_q1(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
        add_tresh_l_q1(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
        add_tresh_l_q1(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        add_tresh_h_q3(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        add_tresh_h_q3(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        add_tresh_l_q3(mass_mode, polarity, scan_type, scan_rate, mass)

    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        add_tresh_l_q3(mass_mode, polarity, scan_type, scan_rate, mass)

    else:
        print('Вы не указали таргетную массу')


df_merge = df_merge.loc[:, ~df_merge.columns.duplicated()]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '16rem',
    'padding': '2rem 1rem',
    'background-color': '#F0F8FF',
}
CONTENT_STYLE = {
    'margin-left': '15rem',
    'margin-right': '2rem',
    'padding': '2rem 1rem',
}
sliderbar = html.Div(
    [
        html.H2('Instrument'),
        html.Hr(),
        html.P(
        'Select device', className = 'lead'
    ),
        # dbc.Nav([
        #     dbc.NavLink('Left\n', href = '/', active = 'exact'),
        #     dbc.NavLink('Right', href = '/page-1', active = 'exact')
        # ],
        # vertical = True,
        # pills = True,
        # ),
    ],
    style = SIDEBAR_STYLE,
)
content = html.Div(id = 'page-content', style = CONTENT_STYLE)

app.layout = html.Div(children=[
    html.H1('Instrument:\nDY260662110', style={'marginLeft':'36rem',
                                               }),
    html.Div([
        dcc.Location(id = 'url'),
        sliderbar,
        content
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


    ], style={
             'boxShadow': '#e3e3e3 4px 4px 2px','marginLeft':'18rem',
             'border-radius': '20px', 'backgroundColor': 'white',
             'width': 150, 'marginTop':'-10rem'}),

    html.Div([
        dcc.Graph(id='graph',
                  )
    ], style={'padding':'.3rem', 'marginTop':'1rem', 'marginLeft':'20rem',
              'boxShadow': '#e3e3e3 4px 4px 2px', 'border-radius': '10px',
              'backgroundColor': 'white', 'width': 550, 'height': 450}),

    html.Div([
        dcc.Graph(id = 'graph_1_1')
    ], style={'padding':'.100rem', 'marginTop':'-45.7rem',
              'marginLeft':'610px', 'boxShadow': '#e3e3e3 4px 4px 2px',
              'border-radius': '10px', 'backgroundColor': 'white',
              'width': 550, 'height': 455, 'left': 1000, 'top': 100}),

    html.Div([
        dcc.Graph(id='graph_2',

                  )
    ],style={'padding':'.3rem', 'marginTop':'2rem',
             'marginLeft':'20rem', 'boxShadow': '#e3e3e3 4px 4px 2px',
             'border-radius': '10px', 'backgroundColor': 'white',
             'width': 550, 'height': 450}),

    html.Div([
        dcc.Graph(id='graph_3')
    ],style={'padding':'.3rem', 'marginTop':'-46rem',
             'marginLeft':'63rem', 'boxShadow': '#e3e3e3 4px 4px 2px',
             'border-radius': '20px', 'backgroundColor': 'white',
             'width': 550, 'height': 440})

])


@app.callback(
    Output('graph', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')
)
def update_graph_1(mass_mode, polarity, scan_type, scan_rate):
    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')

    fig = px.line(df_2, x='time', y='intensity', color='target_mass',
                  color_discrete_sequence=px.colors.qualitative.G10, log_y=True)
    return fig


@app.callback(
    Output('graph_1_1', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')
)
def update_graph_1_1(mass_mode, polarity, scan_type, scan_rate):
    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')

    fig = px.line(df_2, x='time', y='intensity', color='target_mass',
                  color_discrete_sequence=px.colors.qualitative.G10, log_y = True)
    return fig

@app.callback(
    Output('graph_2', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')

)
def update_fig_2(mass_mode, polarity, scan_type, scan_rate):
    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')
    fig = px.line(df_2, x='time', y='width', color='target_mass', color_discrete_sequence=px.colors.qualitative.G10)
    fig.add_hline(0.6)
    fig.add_hline(0.8)
    return fig


@app.callback(
    Output('graph_3', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')

)
def update_fig_3(mass_mode, polarity, scan_type, scan_rate):
    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')
    fig = px.line(df_2, x='time', y='mass_shift', color='target_mass', color_discrete_sequence=px.colors.qualitative.G10)
    return fig

# @app.callback(
#     Output('page-content', 'children'),
#     Input('url', 'pathname')
# )
# def render_page_content(pathname):
#     if pathname == '/':
#         return dbc.NavbarSimple

if __name__ == '__main__':
     app.run_server()

#df = create_df(df_merge, 'High Mass', 'Positive', 'Q1 MS', 10)
#print(tabulate(df_merge.head(), headers='keys'))
print(df_merge['instrument'].unique())