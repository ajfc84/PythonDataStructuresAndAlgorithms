def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


print(power(0.5, 1))

