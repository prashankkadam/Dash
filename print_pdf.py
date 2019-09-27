# -*- coding:/ utf-8 -*-
"""
Created on Tue Jul 23 12:07:20 2019
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
User name - ADM-PKA187
Email ID : prashank.kadam@maersktankers.com
Created on - Wed Jul 31 11:46:22 2019
version : 1.0
"""  
# Importing the required libraries 
import pdfkit
import time

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
time.sleep(5)
pdfkit.from_url('http://127.0.0.1:8050/', r'C:\Users\ADM-PKA187\Desktop\Dastabase\output.pdf',configuration=config, cover_first=True)

# It has to be noted that pdfkit is a good tool to convert your html pages to pdf in python but when you want to 
# convert a dashboard made using a framework like dash, this pdfkit does not work. It always coverts the initial 
# loading page of the dashboard and does not wait for the graphs to be loaded
