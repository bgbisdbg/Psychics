import random

class Psychic:
    def __init__(self, name):
        self.name = name
        self.reliability = 50
        self.guesses = []

    def make_guess(self):
        guess = random.randint(10, 99)
        self.guesses.append(guess)
        return guess

    def update_reliability(self, user_number):
        if self.guesses[-1] == user_number:
            self.reliability += 1
        else:
            self.reliability -= 1

    def to_dict(self):
        return {
            'name': self.name,
            'reliability': self.reliability,
            'guesses': self.guesses,
        }

    @classmethod
    def from_dict(cls, data):
        psychic = cls(data['name'])
        psychic.reliability = data['reliability']
        psychic.guesses = data['guesses']
        return psychic