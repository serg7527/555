from html.entities import html5
import requests
from bs4 import BeautifulSoup
import csv


CSV = 'cards.csv'
HOST = 'https://www.21vek.by'
URL = 'https://www.21vek.by/tires'


HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='style_product__uOVkK')
    tires = []


    for item in items:
        tires.append(
            {
                'tires' : item.find(class_='CardInfo_info__cUeVj style_fullNameContainer__W7Jq4').get_text(),
                'price' : item.find(class_='CardPrice_currentPrice__EU_7r').get_text(),
                'link' : HOST + item.find(class_='CardInfo_info__cUeVj style_fullNameContainer__W7Jq4').find('a').get('href'),
                'pict' : item.find(class_='style_containerImg__PRUiL style_imageContainer__uKgHk').find('img').get('src')
            }
        )
    return tires


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['Название', 'Цена', 'Ссылка', 'Картинка'])
        for item in items:
            writer.writerow([item['tires'], item['price'], item['link'], item['pict']])


def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())

    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсинг страницы: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        
        print('Парсинг окончен')
        #print(cards)
    else:

        print('Error')


parser()