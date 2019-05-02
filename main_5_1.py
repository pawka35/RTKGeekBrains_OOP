'''
модуль для выбора проверяемого задания
'''

from Word import MakeWord as Word
from Sentence import MakeSentense as Sentence


def infoFromSentence(sentence):
    print(f'Слова, составляющие предложение: {sentence.show()}')
    print(f'Части речи слов: {sentence.show_parts()}')
    print(f'Номера слов в предложении: {sentence.content}')


def SentenceFromSent():
    sentence = input('Введите предложение\n')
    listOfWords = []
    for word in sentence.split(' '):
        try:
            currW = Word(word)
        except:
            continue
        listOfWords.append(currW)
    sen = Sentence(listOfWords)
    infoFromSentence(sen)


def SentenseFromWords(needsent=False):
    sent = []
    while True:
        try:
            word = Word(input("Введите слово (exit для остановки)\n"))
        except:
            continue
        if word.text == 'exit':
            break
        else:
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


