# Изучаю GitHub
import certifi
import requests  # импортируем библиотеку requests
from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup

def parse():
    lt=[]
    url = 'https://www.omgtu.ru/general_information/faculties/#:~:text=Омский%20государственный%20технический%20университет%20включает,управления%20(ФЭСиУ)%20Художественно-технологический%20факультет%20(ХТФ)' # передаем необходимы URL адрес
    page = requests.get(url, verify=False)
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, 'html.parser') # передаем страницу в bs4

    tags=soup.find('div', id='pagecontent')

    for tag in tags.findAll('a'):
        lt.append(tag.text.strip())

    file=open('Список факультетов.txt','w')
    for l in lt:
        print(l)
        file.write(l)
        file.write("\n")
    file.close()

    print('Файл "Список факультетов.txt" создан')