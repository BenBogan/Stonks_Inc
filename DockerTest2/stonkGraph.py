import numpy as np
import math
import array
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import pandas_datareader as pdr
import plotly
import plotly.graph_objects as go
import json


#def for pulling a stock
def stock_pull(stock,start,end):
    s = pdr.get_data_yahoo(stock, start= start, end=end)
    return s

## LOADING DATA
#df = pdr.get_data_yahoo(Stock, start= '2020-05-15', end='2020-10-2') #what is this
stock = 'spy'
start = '2020-05-15'
end = '2020-11-20'
df = stock_pull(stock,start,end)

#CALCULATING 20 DAY STD AND MOVING Average
df['20dSTD'] = df.Close.rolling(window=20).std()
df['MA20'] = df.Close.rolling(window=20).mean()

#Calculate the upper and lower bollinger bands
df['Upper'] = df['MA20'] + (df['20dSTD'] * 2)
df['Lower'] = df['MA20'] - (df['20dSTD'] * 2)

#defining PVI
def pvi(tcp, v):
    b = []
    ppvi = 75
    for i in range(N):
        if v[i] > v[i-1]:
            pvi = ppvi + (((tcp[i] - tcp[i-1])/tcp[i-1]) * ppvi)
            ppvi = pvi
            b.append(pvi)
        else:
            b.append(ppvi)
    return b

#pvi varaibles
v = df.Volume
tcp = df.Close
N = len(df.index)

#p_vi data for graph
p_vi = pvi(tcp, v,)

#trace 1 = stock price
trace1 = {
    'x' : df.index,
    #'open' : df.Open,
    'y' : df.Close,
    #'high' : df.High,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'Green'
            },
    #'low': df.Low,
    #'type': 'candlestick',
    'name': stock+' price',
    'showlegend': True
}

#trace 2 = upper bollinger band
trace2 = {
    'x': df.index,
    'y': df['Upper'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
            },
    'name': 'Upper Bollinger Band'
}


# trace 3 = lower bollinger band
trace3 = {
    'x': df.index,
    'y':  df['Lower'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Lower Bollinger Band'
}


#trace4 = moving average
trace4 = {
    'x': df.index,
    'y':  df['MA20'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'yellow'
    },
    'name': 'Moving Average'
}

trace5 = {
    'x': df.index,
    'y':  p_vi,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'Purple'
    },
    'name': 'PVI'
}

#graphing the data
data = [trace1,trace2,trace3,trace4,trace5]
lig = go.Layout({
        'title': {
            'text': stock+' Moving Averages',
            'font':{
                'size':20
            }
        }
})

fig = go.Figure(data = data, layout = lig)

def getfig():
    return fig
fig.show()
