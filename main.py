import requests
from bs4 import BeautifulSoup

def scrap_data():
    url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    data = []
    for item in soup.find_all('div', {'class': 'thumb tright'}):
        data.append(item.text)
    return data

for i in range(len(scrap_data())):
    print(scrap_data()[i])