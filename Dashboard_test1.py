# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
version : 1.0
"""

# Importing the required libraries:
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Test_1')

app.layout = html.Div([
        dcc.Dropdown(
                id = 'my-dropdown',
                options=[
                        {'label': 'Mearsk', 'value': 'MAERSK'},
                        {'label': 'United', 'value': 'UPT'},
                        {'label': 'Hartmann', 'value': 'PHH2'}
                        ],
                value= 'MAERSK'
                ),
        dcc.Graph(id='my-graph')
        ], style={'width': '500'})
        
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
            selected_dropdown_value,
            'google',
            dt(2017, 1, 1),
            dt.now()
            )
    return {
            'data': [{
                    'x': df.index,
                    'y': df.Close
                    }],
    'layout': {'margin': {'l':40, 'r':0, 't':20, 'b':30}}
    }
            
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()            