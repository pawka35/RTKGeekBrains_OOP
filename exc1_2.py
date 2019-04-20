'''
2. Разбейте текст на предложения.
'''
import re

# \.\s - до точки после которой идет пробел

def splitToSentence(text):
    res = re.split('\.\s', text)
    counter = 1
    print('Текст файла, разбитый на предложения: ')
    for x in res:
        if x != "":
            print(f'№{counter}) {x.strip()}')
            counter += 1


if __name__ == '__main__':
    from exs1_1 import fileText
    splitToSentence(fileText('text.txt'))
