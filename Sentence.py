'''
Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''

from WhatPartOfSpeech import whatPartOfSpeech
from Noun import Noun
from Verb import Verb
from Word import Word


class Sentence:
    def __init__(self, words):
        counter = 1
        self.words = words
        self.content = []
        for _ in words:
            self.content.append(counter)
            counter += 1

    def __str__(self):
        message = (f'Слова, составляющие предложение:\n')
        for word in self.words:
            message += f'Слово "{word.text}", часть речи: {word.partOfSpeech}\n'
            message += f'{word.getGramm()}\n'
        message += f'Номера слов в предложении: {str(self.content)}\n'
        return message

    def show(self):
        retList = []
        for w in self.words:
            cur = f'Слово: {w.text}\nЧасть речи:{w.partOfSpeech}'
            try:
                cur += w.getGramm()
            except:
                cur += '\nДля данной части речи описания не предусмотрено'
            retList.append(cur)
        return retList

    def show_parts(self):
        retList = []
        for w in self.words:
            cur = f'Часть речи: {w.partOfSpeech}\n'
            try:
                cur += w.getGramm()
            except:
                cur += '\nДля данной части речи описания не предусмотрено'
            retList.append(cur)
        return retList


def MakeSentense(words):
    return Sentence(words)


if __name__ == '__main__':
    lisOfWords = input('Введите предложение').split()
    sent = []
    for each in lisOfWords:
        pos = whatPartOfSpeech(each)
        if pos == 'существительное':
            newWord = Noun(each, pos)
        elif pos == 'глагол':
            newWord = Verb(each, pos)
        else:
            newWord = Word(each, pos)
        sent.append(newWord)

    sent = Sentence(sent)
    print(sent.content)
    for t in sent.show():
        print(t)
    for t in sent.show_parts():
        print(t)

