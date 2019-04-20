from exs1_1 import fileText
from exs1_1 import readFile
from exc1_2 import splitToSentence
from exc1_3 import wordCount
from exs1_4 import getLinks
from exc1_5 import domenCount
from exs1_6 import changeLinks

fileName = 'text.txt'
func = {
    1: readFile,
    2: splitToSentence,
    3: wordCount,
    4: getLinks,
    5: domenCount,
    6: changeLinks
}


def validateChoise(val):
    try:
        int(val)
        if int(val)>6:
            print('Извините, но у нас всего 6 вариантов.')
            return validateChoise(input('Введите вариант\n'))
    except ValueError:
        print('Введено не число')
        return validateChoise(input('Введите вариант\n'))
    return int(val)


if __name__ == '__main__':
    while True:
        choise = validateChoise(input('Введите вариант\n'))
        if choise == 1:
            func[choise](fileName)
        else:
            func[choise](fileText(fileName))


