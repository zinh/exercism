class Clock(object):
    def __init__(self, hour, minute):
        subtract_hour = 0
        additional_hour = 0
        if minute <= -60:
            subtract_hour = abs(minute // 60)
            self.minute = 60*subtract_hour + minute
        elif minute < 0:
            subtract_hour = 1
            self.minute = 60 + minute
        elif minute >= 60:
            additional_hour = minute // 60
            self.minute = minute % 60
        else:
            self.minute = minute
        aligned_hour = hour - subtract_hour + additional_hour
        if hour < 0:
            day = abs(aligned_hour // 24)
            self.hour = 24*day + aligned_hour
        else:
            self.hour = abs(aligned_hour % 24)

    def __repr__(self):
        return f"{format(self.hour, '02')}:{format(self.minute, '02')}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
