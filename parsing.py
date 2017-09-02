# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 22:32:29 2017

@author: KJH
"""

import requests
import json
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re
LOGIN_INFO = {
    'user_id': 'aa',
    'password': 'aa'
}

    
    #html = first_page.text
    #soup = bs(html, 'html.parser')
    #csrf = soup.find('input', {'name':'_csrf'})
    #print(csrf['value'])
    
    #LOGIN_INFO = {**LOGIN_INFO, **{'_csrf' : csrf['value']}}
    #print (LOGIN_INFO)


def Load_Price():
    try:
        request_price = requests.get('https://bittrex.com/api/v2.0/pub/Markets/GetMarketSummaries').text
        data = json.loads(request_price)
        count=0
        index_neo=0
    
        for item in data['result']:
            if item['Summary']['MarketName']=="BTC-NEO":
                   index_neo = count    
            count = count+1
        
        price_neo = data['result'][index_neo]['Summary']['Last']
        print(price_neo)
     
        #print (index)
    except HTTPError as e:
        print (e)

def Load_TotalMarketCap():
    try:
        request_totalmc = requests.get('https://api.coinmarketcap.com/v1/global/').text
        data = json.loads(request_totalmc)
        print(data['total_market_cap_usd'])

    except HTTPError as e:
        print (e)

Load_Price()
#Load_TotalMarketCap()
        
