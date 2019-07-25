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
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_excel(
    r'M:/Fuel Opt/VesselPerformance/Vessel Information/Vessel Data/Static Data/Prashank/Adara_w_filter_har.xlsx')

def generate_table(dataframe, max_rows=20):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def generate_button():
    return html.Div([
  html.A(html.Button('Download Data', id='download-button'), id='download-link-paid-search-1')
  ])
    
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Static Data'),
    generate_table(df),
    html.Div(style={'padding': 10}),
    generate_button()
])
    
   
'''
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}    
    
html_out = template.render(template_vars)
HTML(string=html_out).write_pdf("report.pdf")
'''  
if __name__ == '__main__':
    app.run_server(debug=True)