def recite(start, take=1):
    current_bottle = start
    verses = []
    for times in range(0, take):
        if current_bottle > 0:
            verses.append(f"{beer(current_bottle)} of beer on the wall, {beer(current_bottle, False)} of beer.")
            verses.append(f"Take {'it' if current_bottle == 1 else 'one'} down and pass it around, {beer(current_bottle - 1, False)} of beer on the wall.")
        else:
            verses.append('No more bottles of beer on the wall, no more bottles of beer.')
            verses.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
        current_bottle = current_bottle - 1 if current_bottle >= 0 else 99
        if times != take - 1:
            verses.append('')
    return verses


def beer(number, cap=True):
    if number >= 2:
        return f'{number} bottles'
    elif number == 1:
        return '1 bottle'
    elif number == 0:
        return 'No more bottles' if cap else 'no more bottles'
    else:
        return '99 bottles'
