'''
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
'''
import re
from collections import Counter

# [а-я,А-Я]{4,} - русские буквы подряд, не менее 4-х


def wordCount(text):
    words=re.findall('[а-я,А-Я]{4,}', text)  # все слова с 4 буквами и более на русском языке
    print('Список слов с 4 и более букв на русском языке:', words, sep='\n')
    countСoincidence=Counter(words)
    print('Подсчет сколько раз слово встречается в тексте:', countСoincidence,
          sep='\n')  # выводим посчитанные повторения
    maxV = max(countСoincidence.values())  # исчем максимальное количество повторений
    print(f'Максимальное количество раз, которое слово повторяется в тексте: {maxV}.')
    print()
    for x in countСoincidence:
        if countСoincidence[x] == maxV:
            print(f'Слово "{x}" встречается в тексте {countСoincidence[x]} раз(а).')


if __name__ == '__main__':
    from exs1_1 import fileText
    wordCount(fileText('text.txt'))


