#To Import US Stock Market Intraday data an convert to Candlestick Analysis in HTML Page using Plotly in the Local Host  

import pandas as pd
import requests
import plotly.graph_objs as go
import plotly

#Make sure the api key txt file saved in the same working directory
def apikey():
    '''Read the Api Key from txt file'''
    f=open('apikey.txt','r+').read()
    return f

def stock_market_html(symbol,interval,apikey):
    '''Using the alphavatage API extracting the US Market historical data.Inside the param Pass the (Ticker,interval,apikey)  '''
    
    # Scrapping the data from the alphavantage database in JASON format
    url = (f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={apikey}&outputsize=full')
    r = requests.get(url)
    data = r.json()

    time_stamp=[]
    open_values=[]
    high_values=[]
    low_values=[]
    close_values=[]
    volume=[]
    #Extracting the values from jason format using the nested for loop concepts and stored in the list above
    for i in data.values(): 
        for j in i.keys():
            time_stamp.append(j)
        for k in i.values():
                if type(k)==dict:
                    open_values.append(k['1. open'])
                    high_values.append(k['2. high'])
                    low_values.append(k['3. low'])
                    close_values.append(k['4. close'])
                    volume.append(k['5. volume'])

    # Using the pandas lib  converting each list to dataframe
    df=pd.DataFrame({'Timestamp':time_stamp[6:],
                     'Open':open_values,
                     'High':high_values,
                     'Low':low_values,
                     'Close':close_values,
                     'Volume':volume})
    
    # Used Plotly graph_obj to give visulation to the dataset
    fig = go.Figure(data=[go.Candlestick(x=df['Timestamp'],
                                        open=df['Open'],
                                        high=df['High'],
                                         low=df['Low'],
                                         close=df['Close']
                                        )])
    #Export candlestick to HTML format
    pt=plotly.offline.plot(fig,filename=(f'{symbol}.html' ))
    
    return pt

result = stock_market_html("MSFT", "1min", apikey())

#Hope this finds usefull