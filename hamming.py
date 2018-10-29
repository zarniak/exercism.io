def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('a')
    else:
        return sum(char_1 != char_2 for char_1, char_2 in zip(strand_a, strand_b))
