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
import plotly.io as pio

WIDTH_0 = 0.6
WIDTH_1 = 0.8
pio.templates.default = 'plotly_white'
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()
conect = Connection(engine, 'tests.txt', 'standards.txt', 'results.txt', 'specifications.txt')
# df_result = conect.create_df_result()
df_merge = conect.create_merge()
df_merge = df_merge.drop('id', axis=1)
df_specification = conect.create_df_specification()

#print(tabulate(df_specification, headers='keys'))


def create_df(df, mass_mode, polarity, scan_type, scan_rate,instrument, mass = None,):
    df = df[(df['instrument'] == instrument)
            &  (df['scan_type'] == scan_type)
            & (df['mass_mode'] == mass_mode)
            & (df['polarity'] == polarity)
            & (df['scan_rate'] == scan_rate)].sort_values(by = ['time']).sort_values(by=['time']).round({'target_mass': 0})

    df['target_mass'] = df['target_mass'].replace('', np.nan).astype('Int64')
    return df

def create_df_spec(df, mass_mode, polarity, scan_type, scan_rate):
    df = df[(df['mass_mode'] == mass_mode)
            & (df['polarity'] == polarity)
            & (df['scan_type'] == scan_type)
            & (df['scan_rate'] == scan_rate)]
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


def add_tresh_h_q1(df, mass_mode, polarity, scan_type, scan_rate):

    if polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)

        return df

    elif polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df


def add_tresh_l_q1(df, mass_mode, polarity, scan_type, scan_rate):

    if polarity == 'Positive' and scan_type == 'Q1 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    if polarity == 'Negative' and scan_type == 'Q1 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df


def add_tresh_h_q3(df, mass_mode,polarity, scan_type, scan_rate):
    if polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    elif polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df


def add_tresh_l_q3(df, mass_mode, polarity, scan_type, scan_rate, mass):
    if polarity == 'Positive' and scan_type == 'Q3 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    elif polarity == 'Negative' and scan_type == 'Q3 MS' and scan_rate == 10:
        df = create_df_spec(df, mass_mode, polarity, scan_type, scan_rate)
        return df


def add_treshold_2(fig,mass_mode, polarity, scan_type):
    if mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':

       fig.add_hline(y = 5e6,line_dash="dash", line_color="green")
       fig.add_hline(y = 50e6,line_dash="dash", line_color="blue")
       fig.add_hline(y=500e6,line_dash="dash", line_color="grey")
       fig.add_hline(y=700e6,line_dash="dash", line_color="black")
       fig.add_hline(y = 800e6,line_dash="dash", line_color="yellow")

       return fig

    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        fig.add_hline(y = 1e6,line_dash="dash", line_color="green")
        fig.add_hline(y = 4e6,line_dash="dash", line_color="blue")
        fig.add_hline(y=10e6,line_dash="dash", line_color="grey")
        fig.add_hline(y=50e6,line_dash="dash", line_color="black")
        fig.add_hline(y = 700e6,line_dash="dash", line_color="yellow")
        return fig

    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':
        fig.add_hline(y=2e6, line_dash="dash", line_color="green")
        fig.add_hline(y=10e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=20e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=70e6, line_dash="dash", line_color="black")
        fig.add_hline(y=500e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=700e6, line_dash="dash", line_color="orange")
        return fig


    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        fig.add_hline(y=1e6, line_dash="dash", line_color="green")
        fig.add_hline(y=6e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=50e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=80e6, line_dash="dash", line_color="black")
        fig.add_hline(y=100e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=300e6, line_dash="dash", line_color="orange")
        fig.add_hline(y=600e6, line_dash="dash", line_color="pink")
        return fig

    elif mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        fig.add_hline(y=1e6, line_dash="dash", line_color="green")
        fig.add_hline(y=9e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=10e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=300e6, line_dash="dash", line_color="black")
        fig.add_hline(y=700e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=900e6, line_dash="dash", line_color="orange")
        return fig



    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        fig.add_hline(y=3e6, line_dash="dash", line_color="green")
        fig.add_hline(y=7e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=9e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=20e6, line_dash="dash", line_color="black")
        fig.add_hline(y=30e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=40e6, line_dash="dash", line_color="orange")
        fig.add_hline(y=400e6, line_dash="dash", line_color="#20B2AA")
        fig.add_hline(y=600e6, line_dash="dash", line_color="#FFEFD5")
        return fig


    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        fig.add_hline(y=3e6, line_dash="dash", line_color="green")
        fig.add_hline(y=7e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=9e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=20e6, line_dash="dash", line_color="black")
        fig.add_hline(y=30e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=40e6, line_dash="dash", line_color="orange")
        fig.add_hline(y=400e6, line_dash="dash", line_color="#20B2AA")
        fig.add_hline(y=600e6, line_dash="dash", line_color="#FFEFD5")
        return fig


    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        fig.add_hline(y=7e6, line_dash="dash", line_color="blue")
        fig.add_hline(y=9e6, line_dash="dash", line_color="grey")
        fig.add_hline(y=20e6, line_dash="dash", line_color="black")
        fig.add_hline(y=30e6, line_dash="dash", line_color="yellow")
        fig.add_hline(y=40e6, line_dash="dash", line_color="orange")
        fig.add_hline(y=400e6, line_dash="dash", line_color="#20B2AA")
        fig.add_hline(y=600e6, line_dash="dash", line_color="#FFEFD5")
        return fig







def add_treshold(df, mass_mode, polarity, scan_type, scan_rate):
    if mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':
        df =add_tresh_h_q1(df, mass_mode, polarity, scan_type, scan_rate)
        return df
    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        df = add_tresh_h_q1(df, mass_mode, polarity, scan_type, scan_rate)
        return df
    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q1 MS':
        df = add_tresh_l_q1(df, mass_mode, polarity, scan_type, scan_rate)
        return df
    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q1 MS':
        df = add_tresh_l_q1(df, mass_mode, polarity, scan_type, scan_rate)
        return df
    elif mass_mode == 'High Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        df = add_tresh_h_q3(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    elif mass_mode == 'High Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        df = add_tresh_h_q3(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    elif mass_mode == 'Low Mass' and polarity == 'Positive' and scan_type == 'Q3 MS':
        df = add_tresh_l_q3(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    elif mass_mode == 'Low Mass' and polarity == 'Negative' and scan_type == 'Q3 MS':
        df = add_tresh_l_q3(df, mass_mode, polarity, scan_type, scan_rate)
        return df

    else:
        print('Вы не указали таргетную массу')


df_merge = df_merge.loc[:, ~df_merge.columns.duplicated()]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
index_page = html.Div([
    dcc.Link('Left', href = '/left'),
    html.Br(),
    dcc.Link('Right', href = '/right')
])
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
        'Select device', className = 'lead',

    ),
        dcc.Link('Left:\nDY260722110', href='/left'),
        html.Br(),
        dcc.Link('Right:\nDY260662110', href='/right')
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


    ], style={
             'boxShadow': '#e3e3e3 4px 4px 2px','marginLeft':'18rem',
             'border-radius': '20px', 'backgroundColor': 'white',
             'width': 150, 'marginTop':'-10rem'}),

    html.Div([
        dcc.Graph(id='graph',
                  )
    ], style={'padding':'.3rem', 'marginTop':'1rem', 'marginLeft':'20rem',
              'boxShadow': '#e3e3e3 4px 4px 2px', 'border-radius': '10px',
              'backgroundColor': 'white', 'width': 1000, 'height': 450}),

    html.Div([
        dcc.Graph(id = 'graph_1_1')
    ], style={'padding':'.100rem', 'marginTop':'4rem',
              'marginLeft':'205px', 'boxShadow': '#e3e3e3 4px 4px 2px',
              'border-radius': '10px', 'backgroundColor': 'white',
              'width': 1000, 'height': 455, 'left': 1000, 'top': 100}),

    html.Div([
        dcc.Graph(id='graph_2')

    ],style={'padding':'.3rem', 'marginTop':'5rem',
             'marginLeft':'20rem', 'boxShadow': '#e3e3e3 4px 4px 2px',
             'border-radius': '10px', 'backgroundColor': 'white',
             'width': 1000, 'height': 450}),

    html.Div([
        dcc.Graph(id='graph_3')
    ],style={'padding':'.3rem', 'marginTop':'5rem',
             'marginLeft':'20rem', 'boxShadow': '#e3e3e3 4px 4px 2px',
             'border-radius': '20px', 'backgroundColor': 'white',
             'width': 1000, 'height': 440})

])
@app.callback(
    Output('graph', 'figure'),
    Input('mass-mode', 'value'),
    Input('polarity-dropdown', 'value'),
    Input('scan_type-dropdown', 'value'),
    Input('scan_rate-dropdown', 'value')
)
def update_graph(mass_mode, polarity, scan_type, scan_rate):

    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')
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
    df_2 = select_target(df_merge, mass_mode, polarity,
                         scan_type, scan_rate, 'DY260662110')
    df_spec = add_treshold(df_specification, mass_mode, polarity, scan_type,scan_rate)
