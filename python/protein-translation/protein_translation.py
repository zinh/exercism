from itertools import takewhile
m = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
        'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

def proteins(strand):                                            
    return list(takewhile(lambda s: s!= 'STOP', [m[strand[pos:pos+3]] for pos in range(0, len(strand), 3)]))
