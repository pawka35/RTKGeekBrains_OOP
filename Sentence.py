'''
Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''

class Sentence:
    content = []
    words = []

    def __init__(self, words):
        counter = 1
        self.words = words
        self.content = []
        for _ in words:
            self.content.append(counter)
            counter += 1

    def show(self):
        return [w.text for w in self.words]

    def show_parts(self):
        return [w.partOfSpeech for w in self.words]


def MakeSentense(words):
    return Sentence(words)


if __name__ == '__main__':
    from Word import MakeWord as Word
    sent = Sentence([Word(w) for w in input('Введите пердложение').split(' ')])
    print(sent.content)
    print(sent.show())
    print(sent.show_parts())

