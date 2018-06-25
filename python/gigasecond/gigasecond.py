from datetime import timedelta
def add_gigasecond(birth_date):
    gigasecond = timedelta(seconds=10**9)
    return birth_date + gigasecond
