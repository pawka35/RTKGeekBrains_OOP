'''
Модуль для чтения текста из файла (эта операция повторяется в нескольких местах, поэтому целесообразно
вынести в отдельный модуль
p.s. также см. main.py
'''


def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == '__main__':
    print(readFile('text.html'))

