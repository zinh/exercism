class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num
        self.valid = self.checksum(card_num)

    def checksum(self, card_num):
        sum_of_digits = 0
        pos = 0
        for num in card_num[::-1]:
            if num != ' ' and (num < '0' or num > '9'):
                return False
            if num >= '0' and num <= '9':
                n = int(num)
                if pos % 2 == 0:
                    sum_of_digits += n
                elif n <= 4:
                    sum_of_digits += n * 2
                else:
                    sum_of_digits += n * 2 - 9
                pos += 1
        return pos > 1 and sum_of_digits % 10 == 0

    def is_valid(self):
        return self.valid
