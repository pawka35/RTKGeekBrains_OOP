'''
4. Отберите все ссылки.
'''

#  [\w*\.]* - домен 3-ого и выще уровней (может и не быть)
#  \w+\.\w+ - сам домен 2=ого уровня и домен 1-ого уровня
#  [\/\w+]* - если есть пути после домена
#  \. - в нашем тексте в конце каждой ссылки стоит точка
import re


def returnShablon():
    return re.compile('([\w*\.]*\w+\.\w+[\/\w+]*)\.')


def getLinks(text):
    links = returnShablon().findall(text)
    print('Список ссылок, содержащихся в тексте:')
    for link in links:
        print(link)


if __name__ == '__main__':
    from exs1_1 import fileText
    getLinks(fileText('text.txt'))
