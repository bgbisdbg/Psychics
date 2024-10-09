from .psychic import Psychic

class PsychicManager:
    def __init__(self, psychics=None):
        self.psychics = psychics or []

    def add_psychic(self, psychic):
        self.psychics.append(psychic)

    def make_guesses(self):
        for psychic in self.psychics:
            psychic.make_guess()

    def update_reliability(self, user_number):
        for psychic in self.psychics:
            psychic.update_reliability(user_number)

    def reset_psychics(self):
        for psychic in self.psychics:
            psychic.reset()

    def clear_psychics(self):
        self.psychics = []

    def to_dict(self):
        return [p.to_dict() for p in self.psychics]

    @classmethod
    def from_dict(cls, data):
        psychics = [Psychic.from_dict(p) for p in data]
        return cls(psychics)