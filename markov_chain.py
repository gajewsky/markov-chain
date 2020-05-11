import fire
from markov_chain.text import Text
from markov_chain.markov_chain import MarkovChain

import csv

def read_dialogs():
    csv_file = open('data/clean_dialog.csv', 'r')
    dialogs = csv.reader(csv_file, delimiter=',', quotechar='"')
    next(dialogs)

    # "title","writer","pony","dialog" for each row

    texts = list()
    for *_, text in dialogs:
      texts.append(text)

    return " ".join(texts)

def sentence_generator(sentence_length = 50, init_state = None):
  dialogs = read_dialogs()
  analyzed_text = Text(dialogs).analyze()

  return MarkovChain(analyzed_text).generate_states(init_state, sentence_length)

if __name__ == '__main__':
  fire.Fire(sentence_generator)
