'''
Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

- от себя - добавил возможность выбора получения информации с сайта, либо с локального сервера
- не получилось запустить локальный сервер из данного скрипта, т.к он стартует и далее ждет подключения, а основной
скрипт перестает выполняться...думал thread поможет...но нет...ждем уроков по многопоточности
...или как правильно решить данный кейс?
'''

import requests
import json

webLink = 'http://api.travelpayouts.com/data/ru/cities.json'
localLink = 'http://127.0.0.1:5000/local_city.json'


def serverChoise():
    while True:
        ch = input('Введите 1 для использование сайта, 2 - для локального файла:\n')
        if ch == '1':
            return requests.get(webLink)
        elif ch == '2':
            print('Не забудте стартовать локальный сервер!')
            return requests.get(localLink)


if __name__ == '__main__':
    a = json.loads(serverChoise().text)
    while True:
        name = input('Введите назвние города (или "список" для перечисления):\n')
        if name.lower() == 'список':
            for each in a:
                print(each['name'], '=', each['code'])
            continue
        matches = [x for x in a if (x['name'] is not None) and (x['name']).lower() == name.lower()]
        if len(matches) > 0:
            print(matches[0]['name'], '=', matches[0]['code'])
        elif len(matches) == 0:
            print('Нет такого города')
        else:
            print('Непридвиденная ошибка')

