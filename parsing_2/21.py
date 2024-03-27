from html.entities import html5
import requests
from bs4 import BeautifulSoup
import csv


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


html = get_html(URL)
print(*get_content(html.text), sep='\n')