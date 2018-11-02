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

    def is_allergic_to(self, item):
        self.item = item
        #item in allergen_list

#    @property
    def lst(self):
        allergen_list = []
        score = self.score
        factors = 7
        while factors >= 0:
            if score >= 2**factors:
                score -= 2**factors
                allergen_list.append(ALLERGENS.get(2**factors))
            factors -= 1
        return allergen_list
        
        
print(Allergies(5).lst())
print(Allergies(5).is_allergic_to('eggs'))
