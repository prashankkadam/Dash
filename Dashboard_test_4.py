"""
# This piece of software is bound by The MIT License (MIT)
# Copyright (c) 2019 Prashank Kadam
# Code written by : Prashank Kadam
# Email ID : prashankkadam07@gmail.com
"""

# Importing required libraries:
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import datetime as dt
import plotly.graph_objs as go

# Initializing the app
app = dash.Dash()

# Declaring the layout
app.layout = html.Div(children=[
    html.H1(children='Polynomial Regression'),
    dcc.Input(id='input',
              placeholder='Enter a value...',
              type='number',
              value=2),  
    html.Button('Submit', id='button'),              
	 dcc.Graph(id='example'),
])

@app.callback(
    dash.dependencies.Output('example', 'figure'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input', 'value')]
)

def update_figure(n_clicks, value):
    
    df = pd.read_excel(r'C:\Users\pasha\Desktop\note.xlsx')
    df['Month_1'] = df['Month'].dt.strftime('%Y-%d-%m')
    df['date_ordinal'] = pd.to_datetime(df['Month_1']).apply(lambda date: date.toordinal())

    x = np.array(df['date_ordinal'])
    y = np.array(df['Sales'])
    
    model = make_pipeline(PolynomialFeatures(value), LinearRegression())
    model.fit(np.array(x).reshape(-1, 1), y)

    #x_reg = np.array(df['date_ordinal'])
    x_reg = np.array(np.arange(737060, 737150, 3))
    y_reg = model.predict(x_reg.reshape(-1, 1))

    new_labels = [dt.date.fromordinal(int(item)) for item in x_reg]

    return {
            'data' : [go.Scatter(
                    x = df['Month_1'],
                    y = y,
                    mode = 'markers'),
                    go.Scatter(
                    x = new_labels,
                    y = y_reg,
                    mode = 'lines')],
            'layout': go.Layout(
            xaxis={
                'title': 'Date'
            },
            yaxis={
                'title': 'Sales'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
            } 
    
# Running the app:    
if __name__ == '__main__':
    app.run_server()