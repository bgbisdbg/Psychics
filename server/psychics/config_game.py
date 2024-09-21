import random
import json

class Game:
    def __init__(self):
        self.psychics_dict = {
            'Экстра-Саня': {
                'rating': 0,
                'predictions': None
            },
            'Всевидящий Борис': {
                'rating': 0,
                'predictions': None
            },
            'Вениамин': {
                'rating': 0,
                'predictions': None
            },
        }

    def start_game(self, number: int):
        self.predictions()
        return self.result(number)

    def predictions(self):
        for psychic in self.psychics_dict:
            self.psychics_dict[psychic]['predictions'] = random.randint(10, 99)

    def result(self, number: int):
        for psychic in self.psychics_dict:
            if self.psychics_dict[psychic]['predictions'] == number:
                self.psychics_dict[psychic]['rating'] += 1
            else:
                self.psychics_dict[psychic]['rating'] -= 1
        return self.get_results()

    def get_results(self):
        results = []
        for psychic, data in self.psychics_dict.items():
            results.append(f"{psychic}: решил что вы загадали {data['predictions']}, рейтинг: {data['rating']},")
        return "\n".join(results)