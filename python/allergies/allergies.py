class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.allergies = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 
                'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 
                'pollen': 64, 'cats': 128}

    def is_allergic_to(self, item):
        return (self.score & self.allergies[item]) == self.allergies[item]

    @property
    def lst(self):
        return [k for k, v in self.allergies.items() if self.is_allergic_to(k)]
