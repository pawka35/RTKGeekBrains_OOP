'''
1. Получите текст из файла.
'''

def fileText(name):
    with open(name, 'r', encoding='utf-8') as f:
        return f.read()


def readFile(name):
    print('Текс из файла:', fileText(name), sep='\n')


if __name__ == '__main__':
    readFile('text.txt')
