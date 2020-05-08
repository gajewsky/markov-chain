import fire
from markov_chain.text import Text
from markov_chain.words_generator import WordsGenerator

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

def sentence_generator(sentence_length = 10, init_word = None):
  dialogs = read_dialogs()
  analyzed_text = Text(dialogs).analyze() 

  return WordsGenerator(analyzed_text, sentence_length, init_word).call   

if __name__ == '__main__':
  fire.Fire(sentence_generator)
