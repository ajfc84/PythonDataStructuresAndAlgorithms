def sum2(n):
    assert n >= 0, 'n must be a positive integer'
    if n == 0:
        return 0
    return n + sum2(n - 1)


print(sum2(2))

