# -*- coding:/ utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
User name - ADM-PKA187
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Jul 30 15:38:21 2019
version : 1.1
"""  

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#import pdfkit
#import time
import base64
import subprocess
import sys

image_filename_1 = r'C:\Users\ADM-PKA187\Desktop\Dastabase\Maersk_Header.png'
encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read())  
image_filename_2 = r'C:\Users\ADM-PKA187\Desktop\Dastabase\Header_2.png'
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read()) 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

Image = html.Div([
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image_1.decode()), height=750, width=1250),
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image_2.decode()), height=750, width=1250)
                ])

body = dbc.Container(
    [
        dbc.Row(
                [
                dbc.Col(
                    [
                        html.H2("AE vs Boiler"),
                        html.P(
                            """\
ME vs AE loss trends
"""
                        ),
                        dbc.Button("View details", color="secondary", id='Button1'),
                        html.Div(id='output-container-button',
                                 children='Enter a value and press submit')
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph 1"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
                ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Graph 2"),
                        dcc.Graph(
                            figure={"data": [go.Scatter(x=[1, 2, 3], y=[3, 1, 2], mode='lines+markers', opacity=0.6),
                                             go.Scatter(x=[1, 2, 3], y=[7, 4, 3], mode='lines+markers', opacity=0.6)]}
                        ),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H2("Graph 3"),
                        dcc.Graph(
                            figure={'data': [go.Bar(x=[1, 2, 3], y=[3, 1, 2], marker=dict(color='skyblue')),
                                             go.Bar(x=[1, 2, 3], y=[0.3, 0.4, 0.1], opacity=1,
                                                    marker=dict(color='skyblue', line=dict(color='black', width=5)))],
                                                    'layout': go.Layout(barmode='overlay')}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app.layout = html.Div([navbar, Image, body])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('Button1', 'n_clicks')]
)
def update_figure(n_clicks):  
    if n_clicks == 1:    
        subprocess.Popen([sys.executable, r'C:\Users\ADM-PKA187\.spyder-py3\Prashank_scripts\print_pdf.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
        return 'Printed'
    if n_clicks == 2:
        return 'Printed twice'

if __name__ == "__main__":
    app.run_server()