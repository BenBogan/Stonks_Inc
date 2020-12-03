# import numpy as np
# import math
# import array
# import matplotlib.pyplot as plt
# import yfinance as yf
# import pandas_datareader as pdr
# import plotly.graph_objects as go
# import os
import robin_stocks as rs
import csv
import pandas as pd
import urllib.request
import json


USERNAME = "ben.bogan.6@gmail.com"
PASSWORD = "Longer!234"

rs.login(username=USERNAME,
         password=PASSWORD,
         expiresIn=86400,
         by_sms=True)

df = pd.read_csv("Full_American_Stock_List.csv")
# print(rs.stocks.get_ratings('SPY'))
list = ['dal', 'aal', 'retard']
with open('not_tradeable_on_rh.csv', 'w') as f:
    writer = csv.writer(f)
    for ticker in (df['Ticker']):
        try:
            quote = rs.stocks.get_stock_quote_by_symbol(ticker)
            response = urllib.request.urlopen(quote['instrument']).read().decode()
            obj = json.loads(response)
            if obj['tradeable'] == False:
                writer.writerow([ticker])
                print(ticker, "     NOT TRADABLE")
            else:
                print(ticker)
        except:
            writer.writerow([ticker])
            print(ticker, "     ERROR")
# not_on_rh=[]
# with open('not_on_rh.csv', 'w') as f:
#     writer = csv.writer(f)
#     for ticker in (df['Ticker']):
#         if rs.stocks.get_earnings(ticker) == []:
#             writer.writerow([ticker])
#         print(ticker)
# rs.logout()
