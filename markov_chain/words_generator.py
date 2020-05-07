from random import choice
from numpy.random import choice as weighted_choice

class WordsGenerator:
    def __init__(self, words, sentence_length = 10, init_word = None):
        self.words = words
        self.sentence_length = sentence_length
        self.init_word = init_word if init_word is not None else choice(list(words.keys()))

    def call(self):
        gen = self.__words_generator()
        words = []
        cnt = 0
        for word in gen:
            cnt += 1

            if cnt >= self.sentence_length or word is None:
                break
            words.append(word)
        words[0] = words[0].capitalize()

        return " ".join(words) + "."

    def __next_word(self, word):
        candidats = self.words[word]

        weights_sum = sum(candidats.values())

        probabilities = list(
            map(lambda x: x / weights_sum, candidats.values())
        )
        next_word = weighted_choice(list(candidats.keys()), 1, p = probabilities)[0]
        return  next_word


    def __words_generator(self):
        word = self.init_word
        while True:
            yield word
            word = self.__next_word(word)