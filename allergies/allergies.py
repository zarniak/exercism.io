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
        self.score = score
        self.allergen_list = self.lst

#    @property
    def lst(self):
        allergen_list = []
        score = self.score % 256
        factors = 7
        while factors >= 0:
            if score >= 2**factors:
                score -= 2**factors
                allergen_list.insert(0, ALLERGENS.get(2**factors))
            factors -= 1
        return allergen_list

    def is_allergic_to(self, item):
        self.item = item

        allergen_list = []
        score = self.score % 256
        factors = 7
        while factors >= 0:
            if score >= 2**factors:
                score -= 2**factors
                allergen_list.append(ALLERGENS.get(2**factors))
            factors -= 1
        return item in allergen_list

    
