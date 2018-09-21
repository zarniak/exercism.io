from datetime import datetime
from datetime import timedelta


def add_gigasecond(birth_date):
    return birth_date + timedelta(seconds=10**9)

print(add_gigasecond(datetime(2011, 4, 25)))
print(add_gigasecond(datetime(1977, 6, 13)))
print(add_gigasecond(datetime(1959, 7, 19)))
print(add_gigasecond(datetime(2015, 1, 24, 22, 0, 0)))
print(add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)))
print(add_gigasecond(datetime(1984, 2, 11)))
