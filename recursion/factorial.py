def factorial(n):
    assert n >= 0, 'factorial number must be a positive integer'
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3.2))


