m = {2: 'two Turtle Doves', 3: 'three French Hens', 
        4: 'four Calling Birds', 5: 'five Gold Rings', 6: 'six Geese-a-Laying', 
        7: 'seven Swans-a-Swimming', 8: 'eight Maids-a-Milking', 9: 'nine Ladies Dancing',
        10: 'ten Lords-a-Leaping', 11: 'eleven Pipers Piping', 12: 'twelve Drummers Drumming'}
numbering = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth', 7: 'seventh', 
        8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh', 12: 'twelfth'}

def recite(start_verse, end_verse):
    return [verse(c) for c in range(start_verse, end_verse + 1)]

def verse(c):
    if c == 1:
        return 'On the first day of Christmas my true love gave to me, a Partridge in a Pear Tree.'
    return ", ".join([f"On the {numbering[c]} day of Christmas my true love gave to me", ', '.join([m[n] for n in range(c, 1, -1)]), "and a Partridge in a Pear Tree."])
