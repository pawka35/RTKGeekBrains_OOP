'''
1. Получить количество учеников с сайта geekbrains.ru:
a) при помощи регулярных

p.s. также см. main.py
'''
import re


def howMuchRe(text):
    number = re.findall('Одногруппники <span>• ([\d]+)</span>', text)
    print(number[0])


def whoTheyRe(text):
    num2 = re.findall('<learning-mates-item>.*?data-name=\"(.*?)\"', text)
    for each in num2:
        print(each)
    # print(len(num2))


def howMuchReMain(text):
    number = re.findall('<span class=\"total-users\">Нас уже (.*?) человек</span>', text)
    print(int(number[0].replace(' ', '')))


if __name__ == '__main__':
    from readfile import readFile
    text = readFile('text.html')
    howMuchRe(text)
    whoTheyRe(text)
    text2 = readFile('main.html')
    howMuchReMain(text2)









