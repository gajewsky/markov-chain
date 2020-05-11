from random import choice
from numpy.random import choice as weighted_choice

class MarkovChain(object):
    def __init__(self, transitions_dict):
        self.transitions_dict = transitions_dict

    def generate_states(self, init_state = None, states_count = 30):
        generator = self.__words_generator(init_state)
        states = [next(generator) for _ in range(states_count)]

        return " ".join(states)

    def __next_state(self, state):
        candidats = self.transitions_dict[state]
        choices = list(candidats.keys())
        weighs = list(candidats.values())
        
        return weighted_choice(choices, p = weighs)

    def __words_generator(self, init_state):
        if init_state is None:
           state = choice(list(self.transitions_dict.keys()))
        else:
            state = init_state
        
        while True:
            yield state
            state = self.__next_state(state)