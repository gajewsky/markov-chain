class Text:
    def __init__(self, input_text):
        self.input_text = input_text
        self.words = self.__count_words()

    def word_stats(self):
        return self.__count_words()

    def __count_words(self):
        split_text = self.input_text.split()
        pairs = self.__each_cons(split_text, 2)
      
        words = {}
        for pair in pairs:
            word = pair[0]
            successor = pair[1]

            if word in words:
                word_successors = words[word]
                if successor in word_successors:
                    count = word_successors[successor]
                    words[word].update({successor: count + 1 })
                else:
                    words[word][successor] = 1
            else:
                words[word] = {successor: 1}

        return words

    def __each_cons(self, x, size):
        return [x[i:i+size] for i in range(len(x)-size+1)]