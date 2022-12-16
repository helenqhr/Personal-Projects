# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 02:26:42 2022

@author: helen

The web scrapper is to grab the list of S&P 500 companies from wikipedia
"""

import requests
from bs4 import BeautifulStoneSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
response = requests.get(url)
t = response.text

soup = BeautifulStoneSoup(t, features = 'lxml')
# print(soup.prettify())

tbody = soup.find_all('tbody')

tickers = []
companies = []
sectors = []
info = {}
count = 503

for i in range(len(tbody[0].contents)):
    if i < 2: 
        continue
    elif i % 2 != 0:
        continue
    else:
        ticker = tbody[0].contents[i].contents[1].text.strip('\n')
        tickers.append(ticker)
        company = tbody[0].contents[i].contents[3].text
        companies.append(ticker)
        sector = tbody[0].contents[i].contents[9].text
        sectors.append(ticker)
    if len(tickers) == count:
        break
    
info ={'Ticker': tickers, 'Company':companies, 'Sector':sectors}
SP500 = pd.DataFrame(info)
print(SP500)
