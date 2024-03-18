from requests_html import HTMLSession

# Создаем объект сессии
session = HTMLSession()

# URL страницы для парсинга
url = 'https://www.example.com'

# Отправляем запрос и получаем страницу
response = session.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Находим все ссылки на странице
    links = response.html.links

    # Выводим найденные ссылки
    for link in links:
        print(link)
else:
    print('Ошибка при получении страницы:', response.status_code)