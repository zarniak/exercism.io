ALLERGENS = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats',
}


class Allergies(object):

    def __init__(self, score):
        self.allergen_list = []
        self.score = score % 256

    @property
    def lst(self):
        factors = 7
        while factors >= 0:
            if self.score >= 2**factors:
                self.score -= 2**factors
                self.allergen_list.insert(0, ALLERGENS.get(2**factors))
            factors -= 1
        return self.allergen_list

    def is_allergic_to(self, item):
        return item in self.lst
