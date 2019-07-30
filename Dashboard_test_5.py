# -*- coding:/ utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
User name - ADM-PKA187
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Jul 30 15:38:21 2019
version : 1.0
"""  

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

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

body = dbc.Container(
    [
        dbc.Row(
                [
                dbc.Col(
                    [
                        html.H2("ME vs AE"),
                        html.P(
                            """\
ME vs AE loss trends
"""
                        ),
                        dbc.Button("View details", color="secondary"),
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
                        html.H2("Ballast vs Laden loss"),
                        html.P(
                            """\
Ballast vs laden loss trends
"""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph 2"),
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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, body])

if __name__ == "__main__":
    app.run_server()