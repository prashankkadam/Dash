# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
version : 1.0
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime as dt

app = dash.Dash('Dashboard_Test_3')

df_init = pd.read_excel('M:\Fuel Opt\VesselPerformance\Vessel Information\Vessel Data\Static Data\Prashank\Adara_w_filter.xlsx')

app.layout = html.Div([
        dcc.DatePickerRange(
        id='my-date-picker-range',
        initial_visible_month=dt(2019, 1, 1),
        end_date=dt(2019, 7, 7)
        ),
        dcc.Dropdown(
                id = 'my-dropdown',
                options=[
                        {'label': 'At Harbor', 'value': 0},
                        {'label': 'At Sea', 'value': 5}
                        ],
                value= 0
                ),
        dcc.Graph(id='my-graph_1'),
        dcc.Graph(id='my-graph_2')
        ], style={'width': '2500'})
  
@app.callback(Output('my-graph_1', 'figure'), 
             [Input('my-dropdown', 'value'),
              Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date')])
def update_graph_1(selected_dropdown_value, start_date, end_date):
    
    df = df_init.loc[(df_init['Type'] == selected_dropdown_value) &\
                     (df_init['Date'].between(start_date, end_date))]
    
    trace_line_1 = go.Scatter(x=df['Date'],
                            y=df['Boiler'],
                            mode='lines+markers',
                            #visible=False,
                            marker={
                                    'size': 15,
                                    'opacity': 0.5,
                                    'line': {'width': 0.5, 'color': 'white'}
                                    },
                            name="Boiler")
    trace_line_2 = go.Scatter(x=df['Date'],
                            y=df['IGG'],
                            mode='lines+markers',
                            #visible=False,
                            marker={
                                    'size': 15,
                                    'opacity': 0.5,
                                    'line': {'width': 0.5, 'color': 'white'}
                                    },
                            name="IGG")
    
    data = [trace_line_1, trace_line_2]
    
    return {
            'data': data,
    'layout': {'margin': {'l':40, 'r':0, 't':20, 'b':30}}
    }      
    
@app.callback(Output('my-graph_2', 'figure'), 
             [Input('my-dropdown', 'value'),
              Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date')])
def update_graph_2(selected_dropdown_value, start_date, end_date):
    
    df = df_init.loc[(df_init['Type'] == selected_dropdown_value) &\
                     (df_init['Date'].between(start_date, end_date))]

    data =  [
            {'x': df['Date'], 'y': df['ME'], 'type': 'bar', 'name' : 'Main Engine'},
            {'x': df['Date'], 'y': df['AE Exp'], 'type': 'bar', 'name': 'Auxillary Engine'},
            ]
    return {
            'data': data,
            'layout': {'margin': {'l':40, 'r':0, 't':20, 'b':30},
                       'bargap': 0.9}
    }  
            
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()     



 
