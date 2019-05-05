'''
класc Word
от себя: переопределен метод __str__ для удобного вывода полей объекта класса
'''

from WhatPartOfSpeech import whatPartOfSpeech


class Word:
    def __init__(self, text, partOfSpeech):
        self.text = text  # записываем в свойство слово, которое нам пришло
        self.partOfSpeech = partOfSpeech

    def __str__(self):
        return (f'Слово: "{self.text}", часть речи: "{self.partOfSpeech}"')


def MakeWord(text):
    return Word(text)


if __name__ == '__main__':
    text = input('Введите слово')
    partOfSpeach = whatPartOfSpeech(text)
    word = Word(text, partOfSpeach)
    print(word)
