DNA_TO_RNA = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
        }


def to_rna(dna_strand):
    return ''.join([DNA_TO_RNA[x] for x in dna_strand])
