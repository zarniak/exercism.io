def prime_factors(natural_number):
    list = []
    x = 2
    while x <= natural_number:
        if natural_number % x == 0:
            list.append(x)
            natural_number = natural_number/x
        else:
            x += 1
    return list
