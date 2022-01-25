from bs4 import BeautifulSoup
import requests

#The headers allow us to see the content of the website
#Placing the investment table into a python object.

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
html_text = requests.get('https://www.forexfactory.com', headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table', class_='calendar__table')
table_rows = soup.find('tbody')

#Scrapping individual pieces of data

date_scrapped = table.find('span', class_='date').text.replace(' ','')
#row = table_rows.find('tr', class_='calendar__row calendar_row calendar__row--grey calendar__row--new-day newday')
currency = table.find_all('td', class_='calendar__cell calendar__currency currency')
currency.append(table.find_all())
print(table.prettify())
print(currency)
#for row in table_rows


print(date_scrapped)
