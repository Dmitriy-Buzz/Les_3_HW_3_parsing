import requests
from bs4 import BeautifulSoup

tags = ['ДТП', 'Спутник']

URL = 'https://www.fontanka.ru'

response = requests.get('https://www.fontanka.ru/')

response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')

all_page =soup.find_all(class_='DZrl')

for n in all_page:
    news = n.find_all(class_='FVdn')
    news = [new.text.strip() for new in news]
    href = n.find(class_='FVdn').attrs.get('href')
    # times = n.find(class_='FVwf')
    # times = [time.text.strip() for time in times]
    for i in news:
        for t in tags:
            if t in i:
                print(f'Название новости "{i}" ссылка на новость:{URL+href}')


# Время публикации {times[0]}