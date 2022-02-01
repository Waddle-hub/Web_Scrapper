from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np

# The headers allow us to see the content of the website
# Placing the investment table into a python object.

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                         'Safari/537.36', 'Referer': 'https://www.forexfactory.com'}
html_text = requests.get('https://www.forexfactory.com', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('div', class_='flexShell')
print(table)

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


