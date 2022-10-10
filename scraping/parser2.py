import datetime
from typing import Dict
from bs4 import BeautifulSoup
from pip import main
import requests as req
from time import sleep
import json


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36 '
}


def search_posts(days) -> Dict:
    '''Функция парсит сайт
    кол-во дней поставить в параметр'''

    data = dict()


    for i in range(-days, 0):
        date = (datetime.date.today() + datetime.timedelta(i)).strftime("%Y/%m/%d")
        print(date)
        
        url = f'https://www.mk.ru/economics/{date}/'
        response = req.get(url=url, headers=HEADERS)
        # sleep(1)
        # response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        posts = soup.find_all(class_="article-listing__item")
        # print(len(posts))
        for art in posts:
            link = art.find(class_="listing-preview__content").get('href')
            views = art.find(class_='meta__item meta__item_views').find(class_='meta__text').text
            title_post = art.find('h3').text.strip()
            preview = art.find(class_='listing-preview__desc').text.replace('\n', '')
            data[link] = {
                'date': date,
                'title_post': title_post,
                'views': views,
                'preview': preview
            }

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return data

if __name__ == '__name__':
    search_posts(700)