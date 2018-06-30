from datetime import date
MeetupDayException = "Wrong format"

def meetup_day(year, month, day_of_the_week, which):
    return get_nth_day(year, month, map_week_day(day_of_the_week), map_day(which))

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
        raise AttributeError(MeetupDayException)

def map_week_day(wd):
    if wd == 'Monday':
        return 0
    if wd == 'Tuesday':
        return 1
    if wd == 'Wednesday':
        return 2
    if wd == 'Thursday':
        return 3
    if wd == 'Friday':
        return 4
    if wd == 'Saturday':
        return 5
    if wd == 'Sunday':
        return 6

# return first Monday/Tuesday/... of a month
def get_first_day(year, month, day_of_week):
    # 0 is Monday, 6 is Sunday
    start_of_month = date(year, month, 1).weekday()
    # first day of month
    if day_of_week == start_of_month:
        return 1
    distance = day_of_week - start_of_month
    distance = distance if distance >= 0 else distance + 7
    return 1 + distance

def get_nth_day(year, month, day_of_the_week, nth):
    first_day = get_first_day(year, month, day_of_the_week)
    if nth == 10:
        for i in range(5):
            d = first_day + i * 7
            if 13 <= d <= 19:
                return date(year, month, d)
    elif nth == 31:
        for i in reversed(range(5)):
            d = first_day + i * 7
            try:
                return date(year, month, d)
            except:
                continue
    else:
        try:
            return date(year, month, first_day + (nth - 1) * 7)
        except:
            raise Exception(MeetupDayException)

# print (meetup_day(2015, 2, 'Monday', '5th'))
