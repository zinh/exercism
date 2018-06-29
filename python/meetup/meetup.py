from datetime import date
MeetupDayException = "Wrong format"

def meetup_day(year, month, day_of_the_week, which):

def map_day(d):
    if d == '1st':
        return 1
    elif d == '2nd':
        return 2
    elif d == '3rd':
        return 3
    elif d == '4th':
        return 4
    elif d == '5th':
        return 5
    elif d == 'teenth':
        return 10
    elif d == 'last':
        return 31
    else:
        raise ValueError('Invalid day of week')

def map_day(year, month, day_of_week):
    # 0 is Monday
    start_of_month = date(year, month, 1).weekday()
    if day_of_the_week != start_of_month:
