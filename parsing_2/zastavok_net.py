import requests
#import fake_useragent
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
#ua = UserAgent(browsers=['edge', 'chrome'])
ua.random

HEADERS = {'User-Agent': ua.chrome}

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


image_number = 0
storage_number = 5
link = f"https://zastavok.net"


for storage in range(4):

    storage_number += 1

    responce = requests.get(f'{link}/{storage_number}').text
    soup = BeautifulSoup(responce, 'html.parser')
    block = soup.find('div', class_ = 'block-photo')
    all_image = block.find_all('div', class_ = 'short_full')

    for image in all_image:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_blok = download_soup.find('div', class_ = 'image_data').find('div', class_ = 'block_down')
        result_link = download_blok.find('a').get('href')

        #Download image
        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'/home/searhei/555/image/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)

        image_number += 1
        print(f'Изображение {image_number}.jpg успешно скачано!')

    