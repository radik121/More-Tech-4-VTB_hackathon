from typing import Dict
from bs4 import BeautifulSoup
from pip import main
import requests as req
from time import sleep
import json

KEYWORDS = []

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36 '
}

def read_post(link: str):
    # Функия читает текст поста изнутри

    res = req.get(link, headers=HEADERS)
    soup_res = BeautifulSoup(res.text, 'lxml')
    return soup_res.find('section', class_='content_page')



def search_posts(pages: int) -> Dict:
    '''Функция парсит сайт
    кол-во страниц поставить в параметр'''

    data = dict()

    for page in range(1, pages+1):
        url = f'https://buh.ru/news/?PAGEN_1={page}'
        response = req.get(url=url, headers=HEADERS)
        sleep(1)
        # response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        posts = soup.find_all(class_="article")
        # return len(posts)
        for art in posts:
            link = 'https://buh.ru' + art.find("a").get('href')
            post = read_post(link)
            number_post = art.get('id').split('_')[-1]
            time_post = post.find(class_='grayd').text
            title_post = post.find('h1').text.strip()
            text_post = post.find(class_='tip-news').text.replace('\n', '')
            data[number_post] = {
                'time_post': time_post,
                'title_post': title_post,
                'link': link,
                'contents': text_post
            }

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return data


def check_new_posts() -> Dict:
    '''Функция проверяет новые новости'''

    fresh_news = dict()

    with open('data.json') as file:
        news_data = json.load(file)

    url = f'https://buh.ru/news/'
    response = req.get(url=url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    posts = soup.find_all(class_="article")
    # return len(posts)
    for art in posts:
        number_post = art.get('id').split('_')[-1]
        
        if number_post in news_data:
            continue
        else:
            link = 'https://buh.ru' + art.find("a").get('href')
            post = read_post(link)
            time_post = post.find(class_='grayd').text
            title_post = post.find('h1').text.strip()
            text_post = post.find(class_='tip-news').text.replace('\n', '')
            fresh_news[number_post] = {
                'time_post': time_post,
                'title_post': title_post,
                'link': link,
                'contents': text_post
            }

    with open('data.json', 'a') as file:
        json.dump(fresh_news, file, indent=4, ensure_ascii=False)

    return fresh_news


if __name__ == '__main__':

    search_posts(300)
    # check_new_posts()
    