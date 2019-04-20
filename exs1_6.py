'''
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
'''

from exs1_4 import returnShablon

def changeLinks(text):
    print(returnShablon().sub('"Ссылка отобразится после регистрации"', text))


if __name__ == '__main__':
    from exs1_1 import fileText
    changeLinks(fileText('text.txt'))
