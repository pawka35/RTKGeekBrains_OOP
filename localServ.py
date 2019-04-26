'''
- локальный сервер, изначально для бытрой отдачи json
- позже добавил немного интерактива, чтобы можно была получить информацию о коде из web интерфейса, используя
локальные данные... чувствую как-то не совсем так то должно выглядеть (шаблоны надо использовать, насколько видел),
но работает...поизучаем еще flask в процессе
'''

from flask import Flask
import json
from flask import request

app = Flask(__name__)


@app.route('/local_city.json')
def getCity():
    with open('local_city.json', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/')
def index():
    with open('countries.json', 'r', encoding='utf-8') as f:
        allcountries = f.read()
    jsonData = json.loads(allcountries)
    text = '''
    <form action="/cities" method="POST">
    <select name = "cities">'''
    for cur in jsonData:
        text += f'<option value = {cur["code"]}>{cur["name"]}</option>'
    text += '</select>'
    text += '<p><input type="submit" value="Отправить"></p></form>'
    return text


@app.route('/cities', methods=['POST'])
def cities():
    result = request.form.getlist('cities')
    counry = result[0]
    with open('local_city.json', 'r', encoding='utf-8') as f:
        allcities = f.read()
    jsonData = json.loads(allcities)

    text = f'''
    <p>Код страны: {counry}</p>
    <hr>
    <p>Выберите город:</p>
    <hr>
       <form action="/getIATA" method="POST">
       <select name = "cities">'''
    for cur in jsonData:
        if cur["country_code"] == counry and cur["name"] != None:
            text+=f'<option value = {cur["code"]}>{cur["name"]}</option>'
    text+='</select>'
    text+='<p><input type="submit" value="Отправить"></p></form>'
    return text


@app.route('/getIATA', methods=['POST'])
def getICAO():
    result = request.form.getlist('cities')
    counry = result[0]
    text = f'''
    <p>Код выбранного города: {counry}</p>
    <hr>
    '''
    return text


def startServer():
    app.run()


if __name__ == '__main__':
    app.run()
