# -*- coding:/ utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
User name - ADM-PKA187
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Jul 30 10:00:14 2019
version : 1.0
"""  


import plotly.graph_objs as go
from plotly.offline import plot


fig = {
    'data': [go.Bar(x=[1, 2, 3], y=[3, 1, 2], marker=dict(color='skyblue')),
             go.Bar(x=[1, 2, 3], y=[0.3, 0.4, 0.1], opacity=1,
             marker=dict(color='rgba(0,0,0,0)', line=dict(color='black', width=5)))],
    'layout': go.Layout(barmode='overlay')
} 

plot(fig)

