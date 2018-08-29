def recite(start_verse, end_verse):
    return [recite_verse(verse) for verse in range(start_verse, end_verse + 1)]

def recite_verse(verse):
    m = [('the house that Jack built', 'lay in'),
         ('the malt','ate'),
         ('the rat','killed'),
         ('the cat','worried'),
         ('the dog','tossed'),
         ('the cow with the crumpled horn','milked'),
         ('the maiden all forlorn','kissed'),
         ('the man all tattered and torn','married'),
         ('the priest all shaven and shorn','woke'),
         ('the rooster that crowed in the morn','kept'),
         ('the farmer sowing his corn','belonged to'),
         ('the horse and the hound and the horn','')]
    return " ".join([f"This is {m[s][0]}" if s == verse - 1 else f"that {m[s][1]} {m[s][0]}" for s in range(0, verse)][::-1]) + '.'
