def prime_factors(natural_number):
    factors = []
    x = 2
    while x <= natural_number:
        if not natural_number % x:
            factors.append(x)
            natural_number /= x
        else:
            x += 1
    return factors
