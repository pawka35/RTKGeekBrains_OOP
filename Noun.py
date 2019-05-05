'''
класс наследуется от Word
в конструкторе используем конструктор базового класса и добавляем приватное поле
переопределяем метод __str__ для удобного вывода информации об объекте
в классе определен метод для получения значения приватного поля
'''

from Word import Word
from WhatPartOfSpeech import whatPartOfSpeech


class Noun(Word):

    def __init__(self, text, partOfSpeech):
        super().__init__(text, partOfSpeech)
        self.__grammChar = '''
Характеристики существительного:
Cклонение(может отсутствовать),Род,Число,Падеж,Одушевлённость(одушевлённое,неодушевлённое), 
Имена(собственное,нарицательное).
'''

    def __str__(self):
        return (f'Слово: "{self.text}", часть речи: "{self.partOfSpeech},\n {self.getGramm()}"')

    def getGramm(self):
        return self.__grammChar


if __name__ == "__main__":
    pof = whatPartOfSpeech("ложка")
    print(pof)
    testW = Noun("ложка", pof)
    print(testW)

