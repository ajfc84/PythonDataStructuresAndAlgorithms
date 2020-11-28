def fibonacci(n):
    assert n >= 0, 'n must be a positive integer'
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5.2))

