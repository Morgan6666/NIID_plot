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
from constant import *
from database_connect import df_merge, df_specification

pio.templates.default = 'plotly_white'


# print(tabulate(df_specification, headers='keys'))
class Selector:
    def __init__(self, df, mass_mode: str, polarity: str, scan_type: str, scan_rate: int,  instrument: str):
        self.df = df
        self.mass_mode = mass_mode
        self.polarity = polarity
        self.scan_type = scan_type
        self.scan_rate = scan_rate
        self.instrument = instrument

    """
        Create DataFrame for  df_merge
    """
    def create_df(self):
        df = self.df[(self.df['instrument'] == self.instrument)
                     & (self.df['scan_type'] == self.scan_type)
                     & (self.df['mass_mode'] == self.mass_mode)
                     & (self.df['polarity'] == self.polarity)
                     & (self.df['scan_rate'] == self.scan_rate)].sort_values(by=['time']).sort_values(
            by=['time']).round({'target_mass': 0})

        df['target_mass'] = df['target_mass'].replace('', np.nan).astype('Int64')
        
        #df_spec = self.add_specification(df)

        return df
    """
        Crete Dataframe for df_spec
    """

    def create_df_spec(self):
        df = self.df[(self.df['mass_mode'] == self.mass_mode)
                     & (self.df['polarity'] == self.polarity)
                     & (self.df['scan_type'] == self.scan_type)
                     & (self.df['scan_rate'] == self.scan_rate)]
        return df

    """
        Select value for Q1 high positive
    """

    def select_q1_high_positive(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df()
            return df

    """
        Select value for Q1  High negative
    """

    def select_q1_high_negative(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df()
            return df

    """
        Select value for Q1 low negative
    """
    def select_q1_low_negative(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df()
            return df

    """
        Select value for Q1 low Positive
    """

    def select_q1_low_positive(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df
            return df


        """
            Select value for Q3 low negative 
        """
    def select_q3_low_negative(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        """
            Select value for Q3 low positive
        """

    def select_q3_low_positive(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_1000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df


        """
            Select value for Q3 High negative
        """
    def select_q3_high_negative(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df()
            return df

        """
            Select value for Q3 High positive
        """

    def select_q3_high_positive(self):
        if self.scan_rate == SCAN_10:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_200:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_2000:
            df = self.create_df()
            return df

        elif self.scan_rate == SCAN_20000:
            df = self.create_df()
            return df


        """
            Select target mass 
        """
    def select_target(self):
        if self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS':
            df = self.select_q1_high_positive()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS':
            df = self.select_q1_high_negative()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS':
            df = self.select_q1_low_positive()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS':
            df = self.select_q1_low_negative()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS':
            df = self.select_q3_high_positive()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS':
            df = self.select_q3_high_negative()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS':
            df = self.select_q3_low_positive()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS':
            df = self.select_q3_low_negative()
            return df


        """
            Add threshold for High Q1
        """
    def add_tresh_h_q1(self):

        if self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

        elif self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

    """
        Add threshold for Low Q1
    """
    def add_tresh_l_q1(self):

        if self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

        if self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

    """
        Add threshold for High Q3
    """
    def add_tresh_h_q3(self):

        if self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

        elif self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == SCAN_10:
            df = self.create_df_spec()
            return df

        """
            Add threshold for Low Q3
        """

    def add_tresh_l_q3(self):

        if self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.create_df_spec()
            return df

        elif self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.create_df_spec()
            return df

    """
        Add Lines threshold
    """
    def add_treshold_2(self, fig):

        if self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS':
            fig.add_hline(y=H_M_P_Q1_500, line_dash="dash", line_color="green")
            fig.add_hline(y=H_M_P_Q1_616, line_dash="dash", line_color="blue")
            fig.add_hline(y=H_M_P_Q1_906, line_dash="dash", line_color="grey")
            fig.add_hline(y=H_M_P_Q1_1952, line_dash="dash", line_color="black")


            return fig

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS':
            fig.add_hline(y=H_M_N_Q1_933, line_dash="dash", line_color="green")
            fig.add_hline(y=H_M_N_Q1_1863, line_dash="dash", line_color="blue")
            return fig

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS':
            fig.add_hline(y=L_M_P_Q1_175, line_dash="dash", line_color="green")
            fig.add_hline(y=L_M_P_Q1_500, line_dash="dash", line_color="blue")
            fig.add_hline(y=L_M_P_Q1_616, line_dash="dash", line_color="grey")
            fig.add_hline(y=L_M_P_Q1_906, line_dash="dash", line_color="black")

            return fig


        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS':
            fig.add_hline(y=L_M_N_Q1_933, line_dash="dash", line_color="green")
            return fig

        elif self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS':
            fig.add_hline(y=H_M_P_Q3_500, line_dash="dash", line_color="green")
            fig.add_hline(y=H_M_P_Q3_616, line_dash="dash", line_color="blue")
            fig.add_hline(y=H_M_P_Q3_906, line_dash="dash", line_color="grey")
            fig.add_hline(y=H_M_P_Q3_1952, line_dash="dash", line_color="black")
            return fig

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS':
            fig.add_hline(y=H_M_N_Q3_933, line_dash="dash", line_color="green")
            fig.add_hline(y=H_M_N_Q3_1863, line_dash="dash", line_color="blue")
            return fig

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS':
            fig.add_hline(y=L_M_P_Q3_175, line_dash="dash", line_color="green")
            fig.add_hline(y=L_M_P_Q3_500, line_dash="dash", line_color="blue")
            fig.add_hline(y=L_M_P_Q3_616, line_dash="dash", line_color="grey")
            fig.add_hline(y=L_M_P_Q3_906, line_dash="dash", line_color="black")
            return fig


        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS':
            fig.add_hline(y=L_M_N_Q3_933, line_dash="dash", line_color="blue")
            return fig


        """
            Add scatter threshold 
        """

    def add_treshold(self):
        if self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df = self.add_tresh_h_q1()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df = self.add_tresh_h_q1()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df = self.add_tresh_l_q1()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df = self.add_tresh_l_q1()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.add_tresh_h_q3()
            return df

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.add_tresh_h_q3()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.add_tresh_l_q3()
            return df

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df = self.add_tresh_l_q3()
            return df

        else:
            print('Вы не указали таргетную массу')




class Private(Selector):
    def add_private(self):

        df = self.create_df()
        if self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df_500_380 = df[df['target_mass'] == 500.380]
            df_500_380['intensity'] = df_500_380['intensity'] / 3.2e7
            df_616_464 = df[df['target_mass'] == 616.464]
            df_616_464['intensity'] = df_616_464['intensity'] / 2.e7
            df_906_673 = df[df['target_mass'] == 906.673] / 9.6e7
            df_906_673['intensity'] = df_906_673['intensity'] / 9.6e7
            df_1952_427 = df[df['target_mass'] == 1952.427]
            df_1952_427['intensity'] = df_1952_427['intensity'] / 2.4e6
            frame = [df_500_380, df_616_464, df_906_673, df_1952_427]
            df_all  = pd.concat(frame).sort_values(by = 'time')
            return df_all

        elif self.mass_mode == 'High Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df_500_380 = df[df['target_mass'] == 500.380]
            df_500_380['intensity'] = df_500_380['intensity'] / 3.2e7
            df_616_464 = df[df['target_mass'] == 616.464]
            df_616_464['intensity'] = df_616_464['intensity'] / 2.e7
            df_906_673 = df[df['target_mass'] == 906.673] / 9.6e7
            df_906_673['intensity'] = df_906_673['intensity'] / 9.6e7
            df_1952_427 = df[df['target_mass'] == 1952.427]
            df_1952_427['intensity'] = df_1952_427['intensity'] / 2.4e6
            frame = [df_500_380, df_616_464, df_906_673, df_1952_427]
            df_all = pd.concat(frame).sort_values(by='time')
            return df_all

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df_933_636 = df[df['target_mass'] == 933.636]
            df_933_636['intensity'] = df_933_636['intensity'] / 1.8e7
            df_1863_306 = df[df['target_mass'] == 1863.306]
            df_1863_306['intensity'] = df_1863_306['intensity'] / 1e6
            frame = [df_1863_306, df_933_636]
            df_all = pd.concat(frame).sort_values(by = 'time')
            return df_all

        elif self.mass_mode == 'High Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df_933_636 = df[df['target_mass'] == 933.636]
            df_933_636['intensity'] = df_933_636['intensity'] / 1.8e7
            df_1863_306 = df[df['target_mass'] == 1863.306]
            df_1863_306['intensity'] = df_1863_306['intensity'] / 1e6
            frame = [df_1863_306, df_933_636]
            df_all = pd.concat(frame).sort_values(by='time')
            return df_all

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df_175_133 = df[df['target_mass'] == 175.133]
            df_175_133['intensity'] = df_175_133['intensity'] / 8.0e6
            df_500_380 = df[df['target_mass'] == 500.380]
            df_500_380['intensity'] = df_500_380['intensity'] / 3.68e7
            df_616_464 = df[df['target_mass'] == 616.464]
            df_616_464['intensity'] = df_616_464['intensity'] / 2.4e7
            df_906_673 = df[df['target_mass'] == 906.673]
            df_906_673['intensity'] = df_906_673['intensity'] / 1.0e8
            df_all = pd.concat(df_175_133, df_500_380, df_616_464, df_906_673).sort_values(by = 'time')
            return df_all

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Positive' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df_175_133 = df[df['target_mass'] == 175.133]
            df_175_133['intensity'] = df_175_133['intensity'] / 8.0e6
            df_500_380 = df[df['target_mass'] == 500.380]
            df_500_380['intensity'] = df_500_380['intensity'] / 3.68e7
            df_616_464 = df[df['target_mass'] == 616.464]
            df_616_464['intensity'] = df_616_464['intensity'] / 2.4e7
            df_906_673 = df[df['target_mass'] == 906.673]
            df_906_673['intensity'] = df_906_673['intensity'] / 1.0e8
            df_all = pd.concat(df_175_133, df_500_380, df_616_464, df_906_673).sort_values(by='time')
            return df_all

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q1 MS' and self.scan_rate == 10:
            df_933_636 = df[df['target_mass'] == 933.636]
            df_933_636['intensity'] = df_933_636['intensity'] / 1.8e7
            return df_933_636

        elif self.mass_mode == 'Low Mass' and self.polarity == 'Negative' and self.scan_type == 'Q3 MS' and self.scan_rate == 10:
            df_933_636 = df[df['target_mass'] == 933.636]
            df_933_636['intensity'] = df_933_636['intensity'] / 1.8e7
            return df_933_636








