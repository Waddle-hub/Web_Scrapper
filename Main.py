from bs4 import BeautifulSoup
import requests
import numpy as np

#The headers allow us to see the content of the website
#Placing the investment table into a python object.

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
html_text = requests.get('https://www.forexfactory.com', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table', class_='calendar__table')
table_rows = soup.find('tbody')

news = table.find_all('td')

#_______________________________________________CURRENCY____________________________________________

currency = table.find_all('td', class_='calendar__cell calendar__currency currency')
for row in currency:
        print(row.text)
print('_________________________________________________________________________________________')

#_______________________________________________DATE________________________________________________

date_scrapped = table.find('span', class_='date').text.replace(' ','')
print(date_scrapped)
print('_________________________________________________________________________________________')

#_______________________________________________NEWS________________________________________________
news = table.find_all('span', class_='calendar__event-title')
for event in news:
    print(event.text)

#_______________________________________________CONSOLIDATE_________________________________________
consolidate = []
consolidate = np.stack((currency, news), axis=1)

print(consolidate)


