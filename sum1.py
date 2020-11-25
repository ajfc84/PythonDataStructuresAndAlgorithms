def sum1(n):
    if n < 10:
        return n
    return n % 10 + sum1(int(n / 10))


print(sum1(123))

