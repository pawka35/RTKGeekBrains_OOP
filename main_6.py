'''
Класс запуска проверки заданий
'''

from Noun import Noun
from Verb import Verb
from WhatPartOfSpeech import whatPartOfSpeech
from Word import Word
from Sentence import Sentence


whatIt = {
    'существительное': Noun,
    'глагол': Verb,
}


def makeWord(word, partOfSpeech):
    if partOfSpeech in whatIt.keys():
        newWord = whatIt[partOfSpeech](word, partOfSpeech)
    else:
        newWord = Word(word, partOfSpeech)
    return newWord


def infoFromSentence(sentence):
    print(sentence)


def SentenceFromSent():
    sentence = input('Введите предложение\n')
    listOfWords = []
    for word in sentence.split(' '):
        try:
            pos = whatPartOfSpeech(word)
            currW = makeWord(word, pos)
        except:
            continue
        listOfWords.append(currW)
    sen = Sentence(listOfWords)
    infoFromSentence(sen)


def SentenseFromWords(needsent=False):
    sent = []
    while True:
        word = input("Введите слово (exit для остановки)\n")
        if word == 'exit':
            break
        else:
            pos = whatPartOfSpeech(word)
            word = makeWord(word,pos)
            print(f'Слово "{word.text}", часть речи - {word.partOfSpeech}')
            if needsent:
                sent.append(word)
    if needsent:
        predl = Sentence(sent)
        infoFromSentence(predl)


if __name__ == '__main__':
    while True:
        choise = input(f'1. Узнать часть речи вводимого слова\n'
                       f'2. Составить предложение из отдельных слов\n'
                       f'3, Разобрать предложение\n'
                       f'Введите номер задачи(q-выход):\n')
        if choise == '1':
            SentenseFromWords()
        elif choise == '2':
            SentenseFromWords(True)
        elif choise == '3':
            SentenceFromSent()
        elif choise == 'q':
            break
        else:
            print(f'Нет такого варианта')

