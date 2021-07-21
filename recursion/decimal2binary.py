def decimal2binary(n):
    assert int(n) == n, 'n must be an integer'
    if n == 0:
        return 0
    return n % 2 + 10 * decimal2binary(int(n / 2))


print(decimal2binary(10))

