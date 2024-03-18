import requests
from bs4 import BeautifulSoup

# URL страницы для парсинга
url = 'https://www.example.com'

# Посылаем GET запрос по указанному URL
response = requests.get(url)

# Проверяем наличие ответа
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Выводим заголовок страницы
    print('Заголовок страницы:', soup.title.text)
    
    # Находим и выводим все ссылки на странице
    links = soup.find_all('a')
    print('Найденные ссылки:')
    for link in links:
        print(link.get('href'))
else:
    print('Ошибка при получении страницы:', response.status_code)