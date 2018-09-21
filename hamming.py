def distance(strand_a, strand_b):
    count = 0
    for i, x in enumerate(strand_a):
        if x != strand_b[i]:
            count = count + 1
    return count
