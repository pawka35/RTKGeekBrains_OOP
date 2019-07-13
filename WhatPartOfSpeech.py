'''
класс для определения части речи введенного слова через запрос к API яндекс-словаря и переводчика
'''

import json
import requests as request


def whatPartOfSpeech(text):
    print(f'Выясняем часть речи слова "{text}"...')
    __apiLangKey = 'trnsl.1.1.20190429T190115Z.d019e52d492eb680.8eb9e705ba8fb831531db623f7a32cb59d8d5473'
    __linkLang = f'https://translate.yandex.net/api/v1.5/tr.json/detect?key={__apiLangKey}&text='
    __apiKey = 'dict.1.1.20190429T181116Z.07cc2bf84959efaf.bc97a1fa25dc3263629f063cea5dda4178afdb17'
    whatLang = f'{__linkLang}{text}'  # составляем ссылку к API я-переводчика для определения на каком языке слово
    try:
        lang = json.loads(request.get(whatLang).text)['lang']  # парсим ответ, получая значение
    except Exception as e:
        print(f'Ошибка определение языка слова, слово "{text}" будет исключено')
        raise

    __link = f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={__apiKey}&lang={lang}-{lang}&ui=ru&' \
        f'&flags=4&text='  # сслыка для запроса к я-словарю, чтобы определить часть речи слова

    apiAnswer = request.get(f'{__link}{text}').text
    try:
        return json.loads(apiAnswer)['def'][0]['pos']  # вытаскиваем часть речи из ответа и заносим в свойство
    except:
        return f'Ошибка определение части речи слово "{text}", слово будет исключено из предложения'
