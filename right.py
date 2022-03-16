import plotly.graph_objects as go
from index_left import app
from dash.dependencies import Input, Output, State
from plot import Selector
from database_connect import df_merge, df_specification
import plotly.express as px
from tabulate import tabulate
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



# if __name__ == '__main__':
#       app.run_server()

import numpy as np
# sel = Selector(df_merge, 'Low Mass', 'Negative', 'Q1 MS', 10,'DY260662110' )
# df = sel.create_df()
#print(tabulate(df_merge.head(),headers='keys' ))
df = df_merge[(df_merge['instrument'] == 'DY260662110')
                      & (df_merge['scan_type'] == 'Q1 MS')
                      & (df_merge['mass_mode'] == 'High Mass')
                      & (df_merge['polarity'] == 'Positive')
                      & (df_merge['scan_rate'] == 10)].sort_values(by=['time']).sort_values(
             by=['time']).round({'target_mass': 0})
#print(df)

