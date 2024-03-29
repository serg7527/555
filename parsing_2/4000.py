import requests
from bs4 import BeautifulSoup


response = requests.get('https://hobbygames.by/warhammer-40000')


soup = BeautifulSoup(response.text, 'html.parser')
data = list(soup.find_all('a', class_='name'))


names = []

for i in range(len(data)):
    tmp_str = str(data[i])
    tmp_str = tmp_str.replace('/a>', "")
    ind = tmp_str.rfind(">")
    tmp_str = tmp_str[ind+1:len(tmp_str)-1]
    tmp_list = tmp_str.split()
    final_name = " ".join(tmp_list)
    names.append(final_name)




print(names)