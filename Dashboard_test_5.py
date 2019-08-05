# -*- coding:/ utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
User name - ADM-PKA187
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Jul 30 15:38:21 2019
version : 1.2
"""  

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import dash_table
from plotly.subplots import make_subplots
#import pdfkit
#import time
import base64
#import subprocess
#import sys

image_filename_1 = r'C:\Users\ADM-PKA187\Desktop\Dastabase\Maersk_Header.png'
encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read())  
image_filename_2 = r'C:\Users\ADM-PKA187\Desktop\Dastabase\Header_2.png'
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read()) 

df = pd.read_excel(r'C:\Users\ADM-PKA187\Desktop\Performance_report\Potential_savings.xlsx')

df2 = pd.read_excel(r'C:\Users\ADM-PKA187\Desktop\Performance_report\df2.xlsx')
df2_temp = df2
df2_temp['Date'] = df2_temp['Date'].dt.month_name()
df2_tran = df2_temp.T
head = ['Month', 'CPH', 'SIN']
df2_tran.insert(loc=0, column='Head', value=head)

df3 = pd.read_excel(r'C:\Users\ADM-PKA187\Desktop\Performance_report\df3.xlsx') 
df3_tran = df3.T
head = ['Vessel Name', 'AE cons.', 'AE baseline']
df3_tran.insert(loc=0, column='Head', value=head)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Print", id='Print'),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Performance Report",
    brand_href="#",
    sticky="top",
)

Image_1 = html.Div([
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image_1.decode()), height=750, width=1183),
                  ])
Image_2 = html.Div([ 
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image_2.decode()), height=750, width=1183),
                  html.H4("Annualised Potential Savings:"),
                  dash_table.DataTable(
                                      id='table',
                                      columns=[{"name": i, "id": i} for i in df.columns],
                                      data=df.to_dict('records'),
                                      ),                                            
                ], style={'padding-bottom':'50px'})

body = dbc.Container(
    [   
        dbc.Row(
                [
                 dbc.Col(
                         html.H3("Fleet Level Overview - Monthly KPI")
                         )]
                ),         
        #Fleet level overview - AE
        dbc.Row(
                [
                 dbc.Col(
                    [
                        html.Div([
                                html.H4("AE Consumption"),
                                dcc.Graph(
                                        figure={"data": [go.Scatter(x=df2['Date'], y=df2['CPH'], mode='lines+markers', opacity=0.6, name="CPH"),
                                             go.Scatter(x=df2['Date'], y=df2['SIN'], mode='lines+markers', opacity=0.6, name="SIN"),
                                             ]}
                                             ),
                                dash_table.DataTable(
                                        id='table_ae',
                                        columns=[{"name": i, "id": i} for i in df2_tran.columns],
                                        data=df2_tran.to_dict('records'),
                                        style_header=dict(display="none"),
                                        style_data_conditional=[
                                                                {
                                                        'if': {'column_id': 'Head'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                                }
                                                                ]
                                )
                                ], style={'padding-bottom':'50px'})
                                        ],  
                                        md=12
                        ),
                    ]
                ),       
        # FLeet level overview Boiler                    
        dbc.Row(
                [
                 dbc.Col(
                    [
                        html.Div([
                                html.H4("Boiler Consumption"),
                                dcc.Graph(
                                        figure={"data": [go.Scatter(x=df2['Date'], y=df2['CPH'], mode='lines+markers', opacity=0.6, name="CPH"),
                                                         go.Scatter(x=df2['Date'], y=df2['SIN'], mode='lines+markers', opacity=0.6, name="SIN"),
                                             ]}
                                             ),
                                dash_table.DataTable(
                                        id='table_blr',
                                        columns=[{"name": i, "id": i} for i in df2_tran.columns],
                                        data=df2_tran.to_dict('records'),
                                        style_header=dict(display="none"),
                                        style_data_conditional=[
                                                                {
                                                        'if': {'column_id': 'Head'},
                                                        'backgroundColor': 'rgb(248, 248, 248)'
                                                                }
                                                                ]
                                )
                                ], style={'padding-bottom':'50px'})
                                        ],  
                                        md=12
                        ),
                    ]
                ),
        #Fleet level overview: Performance when sailing    
        dbc.Row(
                [
                 dbc.Col(
                         html.H4("Performance when Sailing")
                         )]
                ),                    
        dbc.Row(
            [                
                dbc.Col(
                    [
                      html.Div([                                
                              html.H5("AE"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_sail1',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
                dbc.Col(
                    [
                      html.Div([  
                              html.H5("Boiler"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_sail2',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
            ]
        ),
                        
        #Fleet level overview: Performance when not sailing    
        dbc.Row(
                [
                 dbc.Col(
                         html.H4("Performance when not Sailing")
                         )]
                ),                    
        dbc.Row(
            [
                dbc.Col(
                    [
                      html.Div([  
                              html.H5("AE"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_n_sail1',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
                dbc.Col(
                    [
                      html.Div([     
                              html.H5("Boiler"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_n_sail2',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
            ]
        ), 
                                
        #Fleet level overview: kW   
        dbc.Row(
                [
                 dbc.Col(
                         html.H4("kW")
                         )]
                ),                    
        dbc.Row(
            [
                dbc.Col(
                    [
                      html.Div([  
                              html.H5("Performance when not Sailing"),
                              html.H6("AE"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_n_kW1',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
                dbc.Col(
                    [
                      html.Div([  
                              html.H5("Performance when not Sailing"),
                              html.H6("Boiler"),
                              dcc.Graph(
                                      figure={'data': [go.Bar(x=df3['Vessel Name'], y=df3['AE Consumption'], marker=dict(color='skyblue')),
                                                       go.Bar(x=df3['Vessel Name'], y=df3['AE baseline'], opacity=1,
                                                              marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=2)))],                                                  
                                                              'layout': go.Layout(barmode='overlay')}
                                ),
                                dash_table.DataTable(
                                            id='table_n_kW2',
                                            columns=[{"name": i, "id": i} for i in df3_tran.columns],
                                            data=df3_tran.to_dict('records'),
                                            style_header=dict(display="none"),
                                            style_data_conditional=[
                                                                    {
                                                                            'if': {'column_id': 'Head'},
                                                                            'backgroundColor': 'rgb(248, 248, 248)'
                                                                            }
                                                                    ]
                                            ),
                                ], style={'padding-bottom':'50px'})
                                ],
                                md=6,
                                ),
            ]
        ),                                 
    ],
    className="mt-4",
)


app.layout = html.Div([navbar, Image_1, Image_2, body])      

if __name__ == "__main__":
    app.run_server()
