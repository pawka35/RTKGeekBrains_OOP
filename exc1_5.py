'''
5. Ссылки на страницы какого домена встречаются чаще всего?
'''

import re
from collections import Counter

#  [\.|\s] - сначала либо точка(если есть домен 3-ого уровня), либо пробел (если сразу домен 2=ого уровня)
#  \w*)\.\w{2} - домен 2-ого и 1=ого уровня (у нас 1-ого уровня из 2-х букв)
#  [\.|\/] - точка, если заканчивается, либо слэш, если есть продолжение пути ссылки


def domenCount(text):
    domens = re.findall('[\.|\s](\w*\.\w{2})[\.|\/]', text)
    print('В тексте втречаются домены:', domens, sep='\n')
    countСoincidence=Counter(domens)
    print('Считаем повторения:', countСoincidence, sep='\n')  # выводим посчитанные повторения
    maxV = max(countСoincidence.values())  # исчем максимальное количество повторений
    for x in countСoincidence:
        if countСoincidence[x] == maxV:
            print('Ссылка на домен "', x, '" встречается ', countСoincidence[x], ' раз(а).', sep='')


if __name__ == '__main__':
    from exs1_1 import fileText
    domenCount(fileText('text.txt'))