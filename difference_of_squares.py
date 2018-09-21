def square_of_sum(count):
    s = 0
    for x in range(1, count+1):
        s = s + x
    return s**2


def sum_of_squares(count):
    s = 0
    for x in range(1, count+1):
        s = s + x ** 2
    return s


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
print(square_of_sum(1))
print(sum_of_squares(1))
print(difference(1))
print(square_of_sum(5))
print(sum_of_squares(5))
print(difference(5))
print(square_of_sum(100))
print(sum_of_squares(100))
print(difference(100))
