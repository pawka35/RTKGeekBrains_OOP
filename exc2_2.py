'''
1. Получить количество учеников с сайта geekbrains.ru:
b) при помощи библиотеки BeautifulSoup.

p.s. также см. main.py
'''

from bs4 import BeautifulSoup as BS


def howMuchBs(text):
    soup = BS(text, 'html.parser')
    users = soup.find_all('learning-mates-item')
    print(len(users))


def whoTheyAreBs(text):
    import re
    soup = BS(text, 'html.parser')
    a = soup.find_all('learning-mates-item')
    br = re.compile('data-name=\"(.*?)\"')
    users = br.findall(str(a))
    for us in users:
        print(us)


def howMuchBsMain(text):
    soup = BS(text, 'html.parser')
    c = soup.find_all('span', {"class": "total-users"})
    for each in c:
        print(each.string)


if __name__ == '__main__':
    import readfile
    text = readfile.readFile('text.html')
    howMuchBs(text)
    whoTheyAreBs(text)
    text2 = readfile.readFile('main.html')
    howMuchBsMain(text2)


