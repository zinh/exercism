def to_rna(dna_strand):
    h = {'C': 'G', 'G': 'C', 
            'T': 'A',
            'A': 'U'}
    return ''.join(map(lambda c: h[c], dna_strand))
