class Luhn(object):
    def __init__(self, card_num):
        self.card_num = []
        for num in card_num:
            if num != ' ' and (num < '0' or num > '9'):
                self.card_num = []
                break
            elif num >= '0' and num <= '9':
                self.card_num.append(ord(num) - ord('0'))
            else:
                continue
        print(self.card_num)

    def is_valid(self):
        if len(self.card_num) <= 1:
            return False
        s = sum([num if pos % 2 == 0 else num * 2 if num <= 4 else num * 2 - 9 for pos, num in enumerate(self.card_num[::-1])])
        return s % 10 == 0

#l = Luhn("59")
