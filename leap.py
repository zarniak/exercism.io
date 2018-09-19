def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        #https://www.python.org/dev/peps/pep-0008/#indentation
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is NOT a leap year")

#For example, 1997 is not a leap year, but 1996 is.
#1900 is not a leap year, but 2000 is.
#https://www.python.org/dev/peps/pep-0008/#pet-peeves
is_leap_year(1997)
is_leap_year(1996)
is_leap_year(1900)
is_leap_year(2000)
