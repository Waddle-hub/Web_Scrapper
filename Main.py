from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

# _______________________________________________HEADER TESTS____________________________________________

import requests
import random
from collections import OrderedDict

# _______________________________________________HEADER TESTS____________________________________________

# This data was created by using the curl method explained above
headers_list = [
    # Firefox 77 Mac
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Firefox 77 Windows
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Chrome 83 Mac
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    # Chrome 83 Windows
    {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
]

# Create ordered dict from Headers above
ordered_headers_list = []
for headers in headers_list:
    h = OrderedDict()
for header, value in headers.items():
    h[header] = value
ordered_headers_list.append(h)
url = 'https://www.forexfactory.com'
for i in range(1, 4):
    headers = random.choice(headers_list)

# Create a request session
r = requests.Session()
r.headers = headers
response = r.get(url)
print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:" % (i, headers['User-Agent']))
html_text = response.text
print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('div', class_='flexShell')

news = table.find_all('td')

# _______________________________________________CURRENCY____________________________________________

currency = table.find_all('td', class_='calendar__cell calendar__currency currency')
currency_t = []
for row in currency:
    currency_t.append(row.text.strip())
print('_________________________________________________________________________________________')

# _______________________________________________DATE________________________________________________

date_scrapped = table.find('span', class_='date').text.replace(' ', '')
print(date_scrapped)
print('_________________________________________________________________________________________')

# _______________________________________________NEWS________________________________________________

news = table.find_all('span', class_='calendar__event-title')
news_t = []
for event in news:
    news_t.append(event.text)

# _______________________________________________CONSOLIDATE_________________________________________

consolidate = []
consolidate = np.stack((currency_t, news_t), axis=1)
print(consolidate)

# _______________________________________________EXPORT TO EXCEL_____________________________________

# Ensure the Excel file already exists before running
trading_data = pd.DataFrame(consolidate)
trading_data.to_excel(r'C:\**YOUR PATH**\ForexFactoryData.xlsx')
