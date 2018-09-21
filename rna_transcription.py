def to_rna(dna_strand):
    rna = ''
    for x in dna_strand:
        rna = rna + {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
        }[x]
    return rna
print(to_rna('ACGTGGTCTTAA'))
