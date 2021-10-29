import requests
from bs4 import BeautifulSoup
import codecs
import time
import pandas as pd

used_bikes = []

for x in range(0,4000):
    n = int(x)*12
    url = 'https://momotor.id/motor-bekas?offset='
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    r = requests.get(url+str(n), headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    #file = codecs.open('res.html', 'r', 'utf-8')
    #info = file.read()
    #soup = BeautifulSoup(info, 'html.parser')

    contents = soup.find_all('div', {'class': 'card-body'})

    for content in contents:
        try:
            title = content.find('h3', {'class': 'product-name'}).text
            price = content.find('h4', {'class': 'product-price'}).text
            mileage = content.find('div', {'class': 'mileage-wrapper'}).text.strip()
            year = content.find('div', {'class': 'year-wrapper'}).text.strip()
            location = content.find('div', {'class': 'location-wrapper'}).text.strip()
        except:
            pass

        bikes_data = {
            'title': title,
            'price': price,
            'mileage': mileage,
            'year': year,
            'location': location
        }

        used_bikes.append(bikes_data)

    print('bikes found : ', len(used_bikes))
    time.sleep(3)

    df = pd.DataFrame(used_bikes)
    #print(df.head())

    df.to_csv('used_bikes.csv')
    df.to_json('used_bikes.json')
