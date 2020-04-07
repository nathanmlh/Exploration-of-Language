import random


class Generator:
    def __init__(self):
        self.nouns = ["people", "history", "way", "art", "world"]
        self.verbs = ["be", "have", "do", "say", "go"]

    def get_sentence(self):
        return self.get_main_clause()

    def get_main_clause(self):
        return self.get_noun() + " " + self.get_verb()

    def get_noun(self):
        return random.choice(self.nouns)

    def get_verb(self):
        return random.choice(self.verbs)
