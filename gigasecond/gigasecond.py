from datetime import datetime, timedelta


def add_gigasecond(birth_date):
    return birth_date + timedelta(seconds=10**9)
