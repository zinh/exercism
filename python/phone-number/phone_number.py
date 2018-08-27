import re

class Phone(object):
    def __init__(self, phone_number):
        self.area_code, self.exchange_code, self.tail = self.parse(phone_number)
        self.number = self.validate(self.area_code, self.exchange_code, self.tail)

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.tail}"

    def parse(self, phone_number):
        digits = re.findall(r'[0-9]', phone_number)
        if len(digits) == 10:
            return (''.join(digits[0:3]), ''.join(digits[3:6]), ''.join(digits[6:]))
        elif len(digits) == 11 and digits[0] == '1':
            return (''.join(digits[1:4]), ''.join(digits[4:7]), ''.join(digits[7:]))
        raise ValueError('Invalid number')

    def validate(self, area_code, exchange_code, tail):
        if area_code[0] == '0' or area_code[0] == '1' or exchange_code[0] == '0' or exchange_code[0] == '1':
            raise ValueError('Invalid number')
        return area_code + exchange_code + tail
