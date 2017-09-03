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
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import os


class CoinPriceScheduler(object):
    
    def __init__(self):
        self.count = 0
        self.index_neo = 0

    def Load_Price(self):
        try:
            request_price = requests.get('https://bittrex.com/api/v2.0/pub/Markets/GetMarketSummaries').text
            data = json.loads(request_price)
            self.count = 0
    
            for item in data['result']:
                if item['Summary']['MarketName']=="BTC-NEO":
                    index_neo = self.count    
                self.count = self.count+1
        
            price_neo = data['result'][index_neo]['Summary']['Last']
            print(price_neo)
            return price_neo
            
    
        except HTTPError as e:
            print (e)

    def Load_TotalMarketCap(self):
        try:
            request_totalmc = requests.get('https://api.coinmarketcap.com/v1/global/').text
            data = json.loads(request_totalmc)
            print(data['total_market_cap_usd'])
            return data['total_market_cap_usd']

        except HTTPError as e:
            print (e)


    def Start_Scheduler(self):
        scheduler = BlockingScheduler()
        # Official Documents dosen't work with no reason (tried re-install packages after upgrade setuptools)
        trigger = IntervalTrigger(seconds=5) 
        scheduler.add_job(self.Load_Price,trigger)
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
        

    #Load_Price()
    #Load_TotalMarketCap()
        
