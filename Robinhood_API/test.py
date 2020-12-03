# import numpy as np
# import math
# import array
# import matplotlib.pyplot as plt
# import yfinance as yf
# import pandas_datareader as pdr
# import plotly.graph_objects as go
# import os
import csv
import pandas as pd
import robin_stocks as rs
import re

USERNAME = "ben.bogan.6@gmail.com"
PASSWORD = "Longer!234"

rs.login(username=USERNAME,
         password=PASSWORD,
         expiresIn=86400,
         by_sms=True)

df = pd.read_csv("Full_American_Stock_List.csv")

not_on_rh=[]
with open('not_on_rh.csv', 'w') as f:
    writer = csv.writer(f)
    for ticker in (df['Ticker']):
        if rs.stocks.get_earnings(ticker) == []:
            writer.writerow([ticker])
        print(ticker)
# rs.logout()
