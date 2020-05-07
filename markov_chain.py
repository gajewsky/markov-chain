import fire
from markov_chain.text import Text
from markov_chain.words_generator import WordsGenerator

LOREM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text Lorem since the 1500s, when an Lorem printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing"
words = Text(LOREM).word_stats()

if __name__ == '__main__':
  fire.Fire(WordsGenerator(words).call)
