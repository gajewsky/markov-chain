from utils import each_cons

class Text:
    def __init__(self, input_text):
        self.input_text = input_text

    def analyze(self):
        counts = self.__words_with_counted_successors()

        return { k: self.__successors_weights(v)  for k, v in counts.items() }
       
    def __successors_weights(self, successors):
        weights_sum = sum(successors.values())

        return { k: v / weights_sum  for k, v in successors.items() }

    def __words_with_counted_successors(self):
        words = {}
        pairs = self.__pairs()

        for pair in pairs:
            word = pair[0]
            successor = pair[1]

            if word in words:
                self.__update_succesors(words[word], successor)
            else:
                words[word] = { successor: 1 }
        return words
    
    def __update_succesors(self, word_successors, successor):
        if successor in word_successors:
            count = word_successors[successor]
            word_successors.update({ successor: count + 1 })
        else:
            word_successors[successor] = 1

    def __pairs(self):
        split_text = self.input_text.split()
        return each_cons(split_text, 2)