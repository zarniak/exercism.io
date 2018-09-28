dna_to_rna = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
        }


def to_rna(dna_strand):
    return ''.join([dna_to_rna[x] for x in dna_strand])
