'''
основной модуль
- организован цикл для удобной проверки всех заданий
- т.к. не сразу понял, что имеется в виду под списком учеников, то реализовано еще получение кол-ва одногруппников
- реализовано получение списка фамилий одногруппников 2-мя способами
'''


from readfile import readFile
import exc2_1 as exs1
import exc2_2 as exs2


func = {
    1: exs1.howMuchReMain,  # кол-во учеников с главной страницы (регулярные выражения)
    2: exs2.howMuchBsMain,  # кол-во учеников с главной страницы (beautiful soap)
    3: exs1.howMuchRe,  # кол-во одногруппников (регулярные выражниея)
    4: exs2.howMuchBs,  # кол-во одногруппников (beautiful soap)
    5: exs1.whoTheyRe,  # список одногруппников (регулярные выражниея)
    6: exs2.whoTheyAreBs    # список одногруппников (beautiful soap)
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
        print('''
        1 - количество с первой страницы через регулярки
        2 - количество со второй страницы через beautifullsoap
        3 - кол-во одногрупников через регулярки
        4 - кол-во одногруппников через beautifullsoap
        5 - список фамилий одногруппников через регулярки
        6 - список фамилий одногруппников через beautifullsoap
        ''')
        choise = validateChoise(input('Выберите вариант:\n'))
        if choise == 1 or choise == 2:
            text = readFile('main.html')
        else:
            text = readFile('text.html')
        func[choise](text)
        if input('Продолжим?(y/n):\n') == 'n':
            break
