def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # https://www.python.org/dev/peps/pep-0008/#indentation
        return True
    else:
        return False

# For example, 1997 is not a leap year, but 1996 is.
# 1900 is not a leap year, but 2000 is.
# https://www.python.org/dev/peps/pep-0008/#pet-peeves
print(is_leap_year(1997))
print(is_leap_year(1996))
print(is_leap_year(1900))
print(is_leap_year(2000))
